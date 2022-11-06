import socket
from unicodedata import name

s = socket.socket()

s.bind(('DESKTOP-P7Q2KRL', 9999))

s.listen(3)

print("Waiting for connections")
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", addr, name)
    c.close()
