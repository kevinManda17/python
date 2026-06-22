import socket 


host="localhost" ; port=8000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc :
    soc.connect((host,port))
    soc.sendall("Hello kevin".encode("utf-8"))
    buff= soc.recv(2048)
    print(buff.decode("utf-8"))