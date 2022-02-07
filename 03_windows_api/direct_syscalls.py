# Every native API call has a specific number (syscall) that represents it
# https://en.wikipedia.org/wiki/System_call
# kernel32 --> ntdll --> assembly

from ctypes import *
from ctypes import wintypes

# from undocumented_win_api_calls import NtAllocateVirtualMemory

SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

# https://j00ru.vexillium.org/syscalls/nt/64/
# NtAllocateVirtualMemory = 0x0018

# """
# move r10, rcx
# move eax, 18h
# syscall
# ret
# """


def verify(x):
    if not x:
        raise WinError()


buf = create_string_buffer(b"\xb8\x05\x00\x00\x00\xc3")
buf_addr = addressof(buf)
print(hex(buf_addr))

# https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect
VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.LPDWORD)
VirtualProtect.restype = wintypes.INT

# BOOL VirtualProtect(
#   [in]  LPVOID lpAddress,
#   [in]  SIZE_T dwSize,
#   [in]  DWORD  flNewProtect,
#   [out] PDWORD lpflOldProtect
# );
old_protection = wintypes.DWORD(0)
protect = VirtualProtect(
    buf_addr, len(buf), PAGE_EXECUTE_READWRITE, byref(old_protection)
)
verify(protect)

# https://docs.python.org/3/library/ctypes.html
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# The returned function prototype creates functions that use the standard C calling convention. The function will release the GIL during the call.
asm_type = CFUNCTYPE(c_int)
asm_function = asm_type(buf_addr)
r = asm_function()
print(hex(r))

buf2 = create_string_buffer(b"\x4c\x8b\xd1\xb8\x18\x00\x00\x00\x0f\x05\xc3")
buf_addr2 = addressof(buf2)
print("Buffer address 2: ", hex(buf_addr2))

old_protection2 = wintypes.DWORD(0)
protect2 = VirtualProtect(
    buf_addr2, len(buf2), PAGE_EXECUTE_READWRITE, byref(old_protection2)
)
verify(protect2)

# https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntallocatevirtualmemory
# __kernel_entry NTSYSCALLAPI NTSTATUS NtAllocateVirtualMemory(
#   [in]      HANDLE    ProcessHandle,
#   [in, out] PVOID     *BaseAddress,
#   [in]      ULONG_PTR ZeroBits,
#   [in, out] PSIZE_T   RegionSize,
#   [in]      ULONG     AllocationType,
#   [in]      ULONG     Protect
# );

syscall_type = CFUNCTYPE(
    NTSTATUS,
    wintypes.HANDLE,
    POINTER(wintypes.LPVOID),
    wintypes.ULONG,
    POINTER(wintypes.ULONG),
    wintypes.ULONG,
    wintypes.ULONG,
)
syscall_function = syscall_type(buf_addr2)

handle = 0xFFFFFFFFFFFFFFFF
base_address = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)
region_size = wintypes.ULONG(1024 * 12)

ptr2 = syscall_function(
    handle,
    byref(base_address),
    zero_bits,
    byref(region_size),
    MEM_COMMIT | MEM_RESERVE,
    PAGE_EXECUTE_READWRITE,
)

if ptr2 != 0:
    print("error!")
    print(ptr2)

print("Syscall allocation: ", hex(base_address.value))

input()
