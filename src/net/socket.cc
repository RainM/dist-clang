#include <net/socket.h>

#include <base/c_utils.h>
#include <net/end_point.h>

#include <sys/socket.h>

namespace dist_clang {
namespace net {

Socket::Socket(EndPointPtr peer)
    : Data(socket(peer->domain(), peer->type(), peer->protocol())) {
}

bool Socket::Bind(EndPointPtr peer, String* error) {
  if (::bind(native(), *peer, peer->size()) == -1) {
    base::GetLastError(error);
    return false;
  }

  return true;
}

bool Socket::Connect(EndPointPtr peer, String* error) {
  if (connect(native(), *peer, peer->size()) == -1) {
    base::GetLastError(error);
    return false;
  }

  return true;
}

bool Socket::ReuseAddress(String* error) {
  int on = 1;
  if (setsockopt(native(), SOL_SOCKET, SO_REUSEADDR, &on, sizeof(on)) == -1) {
    base::GetLastError(error);
    return false;
  }

  return true;
}

bool Socket::SendTimeout(ui32 sec_timeout, String* error) {
  struct timeval timeout = {sec_timeout, 0};
  constexpr auto size = sizeof(timeout);
  if (setsockopt(native(), SOL_SOCKET, SO_SNDTIMEO, &timeout, size) == -1) {
    base::GetLastError(error);
    return false;
  }

  return true;
}

bool Socket::ReadTimeout(ui32 sec_timeout, String* error) {
  struct timeval timeout = {sec_timeout, 0};
  constexpr auto size = sizeof(timeout);
  if (setsockopt(native(), SOL_SOCKET, SO_RCVTIMEO, &timeout, size) == -1) {
    base::GetLastError(error);
    return false;
  }

  return true;
}

bool Socket::ReadLowWatermark(ui64 bytes_min, String* error) {
  constexpr auto size = sizeof(bytes_min);
  if (setsockopt(native(), SOL_SOCKET, SO_RCVLOWAT, &bytes_min, size) == -1) {
    base::GetLastError(error);
    return false;
  }

  return true;
}

}  // namespace net
}  // namespace dist_clang
