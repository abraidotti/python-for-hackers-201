from ctypes import *

b0 = c_bool(0)
b1 = c_bool(1)

print(b0)
print(type(b0))
print(b1)
print(b1.value)

i0 = c_uint(-1)
print(i0)
print(i0.value)

c0 = c_char_p(b"test")
print(c0.value)

print(c0)
c0 = c_char_p(b"test2")
print(c0.value)

p0 = create_string_buffer(5)
print(p0)
print(p0.raw)
print(p0.value)
p0.value = b"a"
print(p0.raw)
print(p0)

i = c_int(42)
pi = pointer(i)

print(i)
print(pi)
print(pi.contents)

print(p0.value)
print(hex(addressof(p0)))

pt = byref(p0)
print(pt)

print(cast(pt, c_char_p).value)

print(cast(pt, POINTER(c_int)).contents)


class PERSON(Structure):
    _fields_ = [("name", c_char_p), ("age", c_int)]


bob = PERSON(b"bob", 30)
print(bob.name)
print(bob.age)

alice = PERSON(b"alice", 31)
print(alice.name)
print(alice.age)

# you need to initialize arrays first
person_array_t = PERSON * 3
print(person_array_t)

person_array = person_array_t()
person_array[0] = PERSON(b"bob", 30)
person_array[1] = PERSON(b"alice", 31)
person_array[2] = PERSON(b"mallory", 51)
# can't add a fourth due to initializing it with 3!

for person in person_array:
    print(person)
    print(person.name)
