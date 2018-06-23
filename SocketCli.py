import socket
SC=socket.socket()
serADD="127.0.0.1"
port=42315
SC.connect((serADD,port))
while True:
    data=SC.recv(1024)
    data=data.decode()
    print("From Server: "+data)
    break
