import socket , sys 

host= "localhost"
port=50000
counter=0

# we create a socket 
mysocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    mysocket.bind((host,port))
except socket.error:
    print("La liaison du socket a l'adresse choisie a echoue")
    sys.exit()
    
while True :
    print("le serveur pret en attente de requetes...")
    mysocket.listen(10)
    connection , address= mysocket.accept()
    data = connection.recv(4196)
    data= data.decode("utf8")

    print(data)
    connection.close()

mysocket.close()