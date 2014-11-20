#include <base/const_string.h>

#include <base/assert.h>
#include <base/attributes.h>

namespace dist_clang {

namespace {
auto NoopDeleter = [](const char*) {};
auto CharArrayDeleter = std::default_delete<const char[]>();
}

namespace base {

// static
const Literal Literal::empty = "";

ConstString::ConstString(Literal str)
    : str_(str.str_, NoopDeleter), size_(strlen(str.str_)), null_end_(true) {
  DCHECK(str.str_[size_] == '\0');
}

ConstString::ConstString(char str[])
    : str_(str, CharArrayDeleter), size_(strlen(str)), null_end_(true) {
}

ConstString::ConstString(UniquePtr<char[]>& str)
    : str_(str.release(), CharArrayDeleter),
      size_(strlen(str_.get())),
      null_end_(true) {
}

ConstString::ConstString(char str[], size_t size)
    : str_(str, CharArrayDeleter), size_(size) {
}

ConstString::ConstString(UniquePtr<char[]>& str, size_t size)
    : str_(str.release(), CharArrayDeleter), size_(size) {
}

ConstString::ConstString(String&& str)
    : medium_(new String(std::move(str))),
      str_(medium_->data(), NoopDeleter),
      size_(medium_->size()),
      null_end_(true) {
  DCHECK(medium_->data()[size_] == '\0');
}

ConstString::ConstString(String* str) : ConstString(std::move(*str)) {
  DCHECK(str);
  delete str;
}

ConstString::ConstString(Rope&& rope) : rope_(std::move(rope)) {
  for (const auto& str : rope_) {
    size_ += str.size_;
  }
}

ConstString::ConstString(Rope&& rope, size_t hint_size)
    : rope_(std::move(rope)), size_(hint_size) {
}

ConstString::ConstString(const Rope& rope) {
  for (const auto& str : rope) {
    size_ += str.size_;
  }
  rope_ = rope;
}

ConstString::ConstString(const Rope& rope, size_t hint_size)
    : rope_(rope), size_(hint_size) {
}

ConstString::ConstString(const String& str)
    : size_(str.size()), null_end_(true) {
  str_.reset(new char[size_ + 1], CharArrayDeleter);
  memcpy(const_cast<char*>(str_.get()), str.data(), size_ + 1);
  DCHECK(str.data()[size_] == '\0');
}

// static
ConstString ConstString::WrapString(const String& str) {
  return ConstString(str.c_str(), str.size(), true);
}

String ConstString::string_copy(bool collapse) const {
  if (collapse) {
    CollapseRope();
    return String(str_.get(), size_);
  }

  if (rope_.empty()) {
    return String(str_.get(), size_);
  }

  String result;
  result.reserve(size_);

  for (const auto& str : rope_) {
    result += str;
  }

  return result;
}

const char* ConstString::data() const {
  CollapseRope();
  return str_.get();
}

const char* ConstString::c_str() const {
  CollapseRope();
  NullTerminate();
  return str_.get();
}

bool ConstString::operator==(const ConstString& other) const {
  if (size_ != other.size_) {
    return false;
  }
  for (size_t i = 0; i < size_; ++i) {
    if (this->operator[](i) != other[i]) {
      return false;
    }
  }

  return true;
}

size_t ConstString::find(const char* str) const {
  i64 str_size = strlen(str);
  Vector<i64> t(str_size + 1, -1);

  if (str_size == 0) {
    return 0;
  }

  for (i64 i = 1; i <= str_size; ++i) {
    auto pos = t[i - 1];
    while (pos != -1 && str[pos] != str[i - 1]) {
      pos = t[pos];
    }
    t[i] = pos + 1;
  }

  size_t sp = 0;
  i64 kp = 0;
  while (sp < size_) {
    while (kp != -1 && (kp == str_size || str[kp] != this->operator[](sp))) {
      kp = t[kp];
    }
    kp++;
    sp++;
    if (kp == str_size) {
      return sp - str_size;
    }
  }

  return String::npos;
}

const char& ConstString::operator[](size_t index) const {
  DCHECK(index < size_);

  if (!rope_.empty()) {
    for (const auto& str : rope_) {
      if (index < str.size()) {
        return str[index];
      }

      index -= str.size();
    }
  }

  return *(str_.get() + index);
}

ConstString ConstString::operator+(const ConstString& other) const {
  if (!rope_.empty()) {
    Rope rope = rope_;
    rope.push_back(other);
    return rope;
  }

  return Rope{*this, other};
}

ui64 ConstString::GetBlock64(ui64 block_num) const {
  DCHECK(block_num < size_ / 8);

  union {
    char str[8];
    ui64 num;
  } value;

  for (int i = 0; i < 8; ++i) {
    value.str[i] = this->operator[](block_num * 8 + i);
  }

  return value.num;
}

ConstString::ConstString(const char* WEAK_PTR str, size_t size, bool null_end)
    : str_(str, NoopDeleter), size_(size), null_end_(null_end) {
}

void ConstString::CollapseRope() const {
  if (rope_.empty()) {
    return;
  }

  if (rope_.size() == 1) {
    medium_ = rope_.front().medium_;
    str_ = rope_.front().str_;
    null_end_ = rope_.front().null_end_;
  } else {
    str_.reset(new char[size_ + 1], CharArrayDeleter);
    null_end_ = true;

    char* WEAK_PTR ptr = const_cast<char*>(str_.get());
    ptr[size_] = '\0';
    for (const auto& str : rope_) {
      memcpy(ptr, str.str_.get(), str.size_);
      ptr += str.size_;
    }
  }

  rope_.clear();
}

void ConstString::NullTerminate() const {
  if (null_end_) {
    return;
  }

  UniquePtr<char[]> new_str(new char[size_ + 1]);
  new_str[size_] = '\0';
  memcpy(new_str.get(), str_.get(), size_);
  str_.reset(new_str.release(), CharArrayDeleter);
  null_end_ = true;
}

}  // namespace base
}  // namespace dist_clang
