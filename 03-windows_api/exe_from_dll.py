from ctypes import *

# print the time
print(windll.msvcrt.time(None))

# print a thing!
windll.msvcrt.puts(b"Print a thing!")

mut_str = create_string_buffer(10)
print(mut_str.raw)

mut_str.value = b"my string"
print(mut_str.raw)

windll.msvcrt.memset(mut_str, c_char(b"X"), 5)
windll.msvcrt.puts(mut_str)
print(mut_str.raw)
