import socket, sys 

host="localhost"
port= 50000

mysocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    mysocket.connect((host,port))
    print("La connxion au serveur a ete etablie !")
    while True :
        message=input("Entrez un message: ")
        data=f"{message}"
        data= data.encode("utf8")
        mysocket.sendall(data) 
except socket.error:
    print("La connexion a ecchoue ")
    sys.exit()
finally:
    mysocket.close()