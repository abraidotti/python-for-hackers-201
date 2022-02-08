from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
LPCTSTR = c_char_p
SIZE_T = c_size_t

# https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess
OpenProcess = kernel32.OpenProcess
OpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
OpenProcess.restype = wintypes.HANDLE

# https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex
VirtualAllocEx = kernel32.VirtualAllocEx
VirtualAllocEx.argtypes = (
    wintypes.HANDLE,
    wintypes.LPVOID,
    SIZE_T,
    wintypes.DWORD,
    wintypes.DWORD,
)
VirtualAllocEx.restype = wintypes.LPVOID

# https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-writeprocessmemory
WriteProcessMemory = kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = (
    wintypes.HANDLE,
    wintypes.LPVOID,
    wintypes.LPVOID,
    SIZE_T,
    POINTER(SIZE_T),
)
WriteProcessMemory.restype = wintypes.BOOL

# https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlea
GetModuleHandleA = kernel32.GetModuleHandleA
GetModuleHandleA.argtypes = (LPCTSTR,)
GetModuleHandleA.restype = wintypes.HANDLE

# https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress
GetProcAddress = kernel32.GetProcAddress
GetProcAddress.argtypes = (wintypes.HANDLE, LPCTSTR)
GetProcAddress.restype = wintypes.LPVOID

# https://docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)
# needed in CreateRemoteThread down below...
class _SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ("nLength", wintypes.DWORD),
        ("lpSecurityDescriptor", wintypes.LPVOID),
        ("bInheritHandle", wintypes.BOOL),
    ]


SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES
LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)
LPTHREAD_START_ROUTINE = wintypes.LPVOID

# https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread
CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.argtypes = (
    wintypes.HANDLE,
    LPSECURITY_ATTRIBUTES,
    SIZE_T,
    LPTHREAD_START_ROUTINE,
    wintypes.LPVOID,
    wintypes.DWORD,
    wintypes.LPDWORD,
)
CreateRemoteThread.restype = wintypes.HANDLE

# https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex#parameters
MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000

# https://docs.microsoft.com/en-us/windows/win32/memory/memory-protection-constants
PAGE_READWRITE = 0x04

# no idea where this is from
EXECUTE_IMMEDIATELY = 0x0

# https://docs.microsoft.com/en-us/windows/win32/procthread/process-security-and-access-rights
# this below value does not match current docs
PROCESS_ALL_ACCESS = 0x000F0000 | 0x00100000 | 0x00000FFF

dll = b".\\HELLO_WORLD.dll"
pid = 21940

handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

if not handle:
    raise WinError()

print("Handle obtained: {0:X}".format(handle))

# https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex
remote_memory = VirtualAllocEx(
    handle, False, len(dll) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE
)

if not remote_memory:
    raise WinError()

print("Memory allocated: ", hex(remote_memory))

write = WriteProcessMemory(handle, remote_memory, dll, len(dll) + 1, None)

if not write:
    raise WinError()

print("Bytes written => {}".format(dll))

# https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress
load_lib = GetProcAddress(GetModuleHandleA(b"kernel32.dll"), b"LoadLibraryA")

print("LoadLibrary address => ", hex(load_lib))

# https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread
remote_thread = CreateRemoteThread(
    handle, None, 0, load_lib, remote_memory, EXECUTE_IMMEDIATELY, None
)

print(remote_thread)
