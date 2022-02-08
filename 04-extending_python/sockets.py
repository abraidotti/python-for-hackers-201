# https://docs.python.org/3/library/socket.html
import socket

ip = socket.gethostbyname("247ctf.com")
print(ip)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("247ctf.com", 80))

# send a GET request without a body
s.sendall(b"HEAD / HTTP/1.1\r\nHost: 247ctf.com\r\n\r\n")

# print out what comes back
print(s.recv(1024).decode())

client = False
server = False
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# warning - this might hang in the terminal
if server:
    # listen by using 'bind' first
    s.bind(("127.0.0.1", port))
    s.listen()

    while True:
        # return values from accept are a new socket object
        connect, add = s.accept()
        connect.send(b"You made it to the socket!")
        connect.close()

if client:
    s.connect(("127.0.0.1", port))
    print(s.recv(1024))
    s.close()

for port in [22, 80, 139, 443, 445, 8080]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    # connect_ex is like connect but returns an error
    # instead of raising an exception
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        print(f"{port} is open!")
    else:
        print(f"{port} is closed.")
