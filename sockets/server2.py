import socket

host='localhost'
port=4000
#create connection  from outside 
serversoc= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversoc.bind((host,port))

print("le serveur est en marche...")

while True :
    serversoc.listen(10)
    client_soc, address=serversoc.accept()
    print("le serveur est en ecoute...",f"client{client_soc} address{address}")

    data=client_soc.recv(4196)
    data=data.decode('utf8')
    print(data)
    client= True
    while client== False :
        client_soc.close()

serversoc.close()