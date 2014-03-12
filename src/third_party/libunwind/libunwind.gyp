{
  'includes': [
    '../../build/configs.gypi',
  ],

  'targets': [
    {
      'target_name': 'unwind',
      'type': 'static_library',
      'defines': [
        '_GNU_SOURCE',
        'CONSERVATIVE_CHECKS',
        'HAVE___THREAD',
        'HAVE__BUILTIN___CLEAR_CACHE',
        'HAVE__BUILTIN_UNREACHABLE',
        'HAVE_BYTESWAP_H',
        'HAVE_DECL_PT_CONTINUE',
        'HAVE_DECL_PT_GETFPREGS',
        'HAVE_DECL_PT_GETREGS',
        'HAVE_DECL_PT_STEP',
        'HAVE_DECL_PT_SYSCALL',
        'HAVE_DECL_PT_TRACE_ME',
        'HAVE_DECL_PTRACE_CONT',
        'HAVE_DECL_PTRACE_POKEDATA',
        'HAVE_DECL_PTRACE_POKEUSER',
        'HAVE_DECL_PTRACE_SINGLESTEP',
        'HAVE_DECL_PTRACE_SYSCALL',
        'HAVE_DECL_PTRACE_TRACEME',
        'HAVE_DL_ITERATE_PHDR',
        'HAVE_DLFCN_H',
        'HAVE_ELF_H',
        'HAVE_ENDIAN_H',
        'HAVE_EXECINFO_H',
        'HAVE_INTTYPES_H',
        'HAVE_LINK_H',
        'HAVE_LZMA',
        'HAVE_MEMORY_H',
        'HAVE_MINCORE',
        'HAVE_SIGNAL_H',
        'HAVE_STDINT_H',
        'HAVE_STDLIB_H',
        'HAVE_STRING_H',
        'HAVE_STRINGS_H',
        'HAVE_STRUCT_DL_PHDR_INFO_DLPI_SUBS',
        'HAVE_STRUCT_ELF_PRSTATUS',
        'HAVE_SYNC_ATOMICS',
        'HAVE_SYS_PROCFS_H',
        'HAVE_SYS_PTRACE_H',
        'HAVE_SYS_STAT_H',
        'HAVE_SYS_TYPES_H',
        'HAVE_UNISTD_H',
        'PACKAGE_BUGREPORT="libunwind-devel@nongnu.org"',
        'PACKAGE_STRING ="libunwind 1.1"',
        'SIZEOF_OFF_T=8',
        'STDC_HEADERS',
      ],
      'include_dirs': [
        'include',
        'include/tdep-x86_64',
        'src',
      ],
      'cflags': [
        '-fexceptions',
        '-fPIC',
        '-Wall',
        '-Wsign-compare',
        '-Wno-header-guard',
      ],
      'cflags!': [
        '-fno-exceptions',
      ],
      'ldflags': [
        '-nostdlib',
      ],
      'ldflags!': [
        '-fno-exceptions',
      ],
      'link_settings': {
        'libraries': [
          '-lc',
          '-llzma',
        ],
      },
      'sources': [
        'src/mi/_ReadULEB.c',
        'src/mi/_ReadSLEB.c',
        'src/mi/backtrace.c',
        'src/mi/dyn-cancel.c',
        'src/mi/dyn-info-list.c',
        'src/mi/dyn-register.c',
        'src/mi/flush_cache.c',
        'src/mi/init.c',
        'src/mi/Ldestroy_addr_space.c',
        'src/mi/Ldyn-extract.c',
        'src/mi/Lfind_dynamic_proc_info.c',
        'src/mi/Lget_accessors.c',
        'src/mi/Lget_fpreg.c',
        'src/mi/Lget_proc_info_by_ip.c',
        'src/mi/Lget_proc_name.c',
        'src/mi/Lget_reg.c',
        'src/mi/Lput_dynamic_unwind_info.c',
        'src/mi/Lset_caching_policy.c',
        'src/mi/Lset_fpreg.c',
        'src/mi/Lset_reg.c',
        'src/mi/mempool.c',
        'src/mi/strerror.c',
        'src/os-linux.c',
        'src/unwind/Backtrace.c',
        'src/unwind/DeleteException.c',
        'src/unwind/FindEnclosingFunction.c',
        'src/unwind/ForcedUnwind.c',
        'src/unwind/GetBSP.c',
        'src/unwind/GetCFA.c',
        'src/unwind/GetDataRelBase.c',
        'src/unwind/GetGR.c',
        'src/unwind/GetIP.c',
        'src/unwind/GetIPInfo.c',
        'src/unwind/GetLanguageSpecificData.c',
        'src/unwind/GetRegionStart.c',
        'src/unwind/GetTextRelBase.c',
        'src/unwind/RaiseException.c',
        'src/unwind/Resume.c',
        'src/unwind/Resume_or_Rethrow.c',
        'src/unwind/SetGR.c',
        'src/unwind/SetIP.c',
        'src/x86_64/getcontext.S',
        'src/x86_64/is_fpreg.c',
        'src/x86_64/Lcreate_addr_space.c',
        'src/x86_64/Lget_proc_info.c',
        'src/x86_64/Lget_save_loc.c',
        'src/x86_64/Lglobal.c',
        'src/x86_64/Linit.c',
        'src/x86_64/Linit_local.c',
        'src/x86_64/Linit_remote.c',
        'src/x86_64/Los-linux.c',
        'src/x86_64/Lregs.c',
        'src/x86_64/Lresume.c',
        'src/x86_64/Lstash_frame.c',
        'src/x86_64/Lstep.c',
        'src/x86_64/Ltrace.c',
        'src/x86_64/regname.c',
        'src/x86_64/setcontext.S',

        # dwarf-generic + dwarf-common + dwarf-local
        'src/dwarf/global.c',
        'src/dwarf/Gexpr.c',
        'src/dwarf/Gfde.c',
        'src/dwarf/Gparser.c',
        'src/dwarf/Gpe.c',
        'src/dwarf/Gstep.c',
        'src/dwarf/Gfind_proc_info-lsb.c',
        'src/dwarf/Gfind_unwind_table.c',
        'src/dwarf/Lexpr.c',
        'src/dwarf/Lfde.c',
        'src/dwarf/Lfind_proc_info-lsb.c',
        'src/dwarf/Lfind_unwind_table.c',
        'src/dwarf/Lparser.c',
        'src/dwarf/Lpe.c',
        'src/dwarf/Lstep.c',

        # elf64
        'src/elf64.c',
        'src/elf64.h',
        'src/elfxx.h',

        # libunwind-x86_64
        'src/mi/Gdyn-extract.c',
        'src/mi/Gdyn-remote.c',
        'src/mi/Gfind_dynamic_proc_info.c',
        'src/mi/Gget_proc_info_by_ip.c',
        'src/mi/Gget_proc_name.c',
        'src/mi/Gput_dynamic_unwind_info.c',
        'src/mi/Gdestroy_addr_space.c',
        'src/mi/Gget_reg.c',
        'src/mi/Gset_reg.c',
        'src/mi/Gget_fpreg.c',
        'src/mi/Gset_fpreg.c',
        'src/mi/Gset_caching_policy.c',
        'src/mi/init.c',
        'src/mi/flush_cache.c',
        'src/mi/mempool.c',
        'src/mi/strerror.c',
        'src/os-linux.c',
        'src/x86_64/Gcreate_addr_space.c',
        'src/x86_64/Gget_save_loc.c',
        'src/x86_64/Gglobal.c',
        'src/x86_64/Ginit.c',
        'src/x86_64/Ginit_local.c',
        'src/x86_64/Ginit_remote.c',
        'src/x86_64/Gget_proc_info.c',
        'src/x86_64/Gregs.c',
        'src/x86_64/Gresume.c',
        'src/x86_64/Gstash_frame.c',
        'src/x86_64/Gstep.c',
        'src/x86_64/Gtrace.c',
        'src/x86_64/Gos-linux.c',
        'src/x86_64/is_fpreg.c',
        'src/x86_64/regname.c',
      ],
    },
  ],
}