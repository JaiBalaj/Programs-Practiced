import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 12349
s.connect(('192.168.225.221', port))
while 1:
    print(s.recv(1024).decode())
    inp = input()
    s.send(inp.encode())
s.close()