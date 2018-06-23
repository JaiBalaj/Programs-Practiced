import socket
SS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serADD="127.0.0.1"
port=42315
SS.bind((serADD,port))
SS.listen(5)
while True:
    CliADD,arr=SS.accept()
    print('Thanks For Connecting: ',arr)
    CliADD.send('Hello Client'.encode())
    print("Server Exiting !")
    break