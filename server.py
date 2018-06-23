import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket successfully created")
port = 12349
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    while 1:
        s=input()
        c.send(s.encode())
        print((c.recv(1024)).decode())
    c.close()