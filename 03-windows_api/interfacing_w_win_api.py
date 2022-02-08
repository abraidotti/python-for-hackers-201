# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxa
# int MessageBoxA(
#   [in, optional] HWND   hWnd,
#   [in, optional] LPCSTR lpText,
#   [in, optional] LPCSTR lpCaption,
#   [in]           UINT   uType
# );

# https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-getusernamea
# BOOL GetUserNameA(
#   [out]     LPSTR   lpBuffer,
#   [in, out] LPDWORD pcbBuffer
# );

from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL

MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype = INT

print(MessageBoxA)

lpText = LPCSTR(b"World")
lpCaption = LPCSTR(b"Hello")
MB_OK = 0x00000000
MB_OKCANCEL = 0x00000001

# MessageBoxA(None, lpText, lpCaption, MB_OKCANCEL)

GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = (LPSTR, LPDWORD)
GetUserNameA.restype = INT

# buffer_size = DWORD(8)
# 'alessandro' will error out with DWORD of only 8
buffer_size = DWORD(16)
buffer = create_string_buffer(buffer_size.value)

# use byref because LPDWORD is a pointer
GetUserNameA(buffer, byref(buffer_size))
print(buffer.value)

# https://docs.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror
# _Post_equals_last_error_ DWORD GetLastError();

error = GetLastError()

if error:
    print(error)
    print(WinError(error))
    # 122
    # https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-
    # The data area passed to a system call is too small.


# make a RECT structure
# https://docs.microsoft.com/en-us/windows/win32/api/windef/ns-windef-rect
# typedef struct tagRECT {
#   LONG left;
#   LONG top;
#   LONG right;
#   LONG bottom;
# } RECT, *PRECT, *NPRECT, *LPRECT;


class RECT(Structure):
    _fields_ = [
        ("left", c_long),
        ("right", c_long),
        ("top", c_long),
        ("bottom", c_long),
    ]


rect = RECT()

print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)

rect.left = 1
print(rect.left)

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowrect
# Retrieves the dimensions of the bounding rectangle of the specified window. The
# dimensions are given in screen coordinates that are relative to the upper-left corner
# of the screen.
# BOOL GetWindowRect(
#   [in]  HWND   hWnd,
#   [out] LPRECT lpRect
# );

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = (HANDLE, POINTER(RECT))
GetWindowRect.restype = BOOL

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getforegroundwindow
hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd, byref(rect))

print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)
