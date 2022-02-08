# https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc
# Reserves, commits, or changes the state of a region of pages in the virtual address space of the calling process.
# Memory allocated by this function is automatically initialized to zero.


from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
SIZE_T = c_size_t

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAlloc.restype = wintypes.LPVOID

# LPVOID VirtualAlloc(
#   [in, optional] LPVOID lpAddress,
#   [in]           SIZE_T dwSize,
#   [in]           DWORD  flAllocationType,
#   [in]           DWORD  flProtect
# );

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
# https://docs.microsoft.com/en-us/windows/win32/memory/memory-protection-constants
PAGE_EXECUTE_READWRITE = 0x40

ptr = VirtualAlloc(None, 1024 * 4, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

error = GetLastError()

if error:
    print(error)
    print(WinError(error))

print("VirtualAlloc: ", hex(ptr))

# https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntallocatevirtualmemory
# __kernel_entry NTSYSCALLAPI NTSTATUS NtAllocateVirtualMemory(
#   [in]      HANDLE    ProcessHandle,
#   [in, out] PVOID     *BaseAddress,
#   [in]      ULONG_PTR ZeroBits,
#   [in, out] PSIZE_T   RegionSize,
#   [in]      ULONG     AllocationType,
#   [in]      ULONG     Protect
# );

nt = windll.ntdll
NTSTATUS = wintypes.DWORD
NtAllocateVirtualMemory = nt.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = (
    wintypes.HANDLE,
    POINTER(wintypes.LPVOID),
    wintypes.ULONG,
    POINTER(wintypes.ULONG),
    wintypes.ULONG,
    wintypes.ULONG,
)
NtAllocateVirtualMemory.restype = NTSTATUS

# https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess
handle = 0xFFFFFFFFFFFFFFFF
base_address = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)
region_size = wintypes.ULONG(1024 * 12)

ptr2 = NtAllocateVirtualMemory(
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

print("NtAllocateVirtualMemory: ", hex(base_address.value))

input()
