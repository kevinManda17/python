import socket 

host ,port =("localhost", 3000)

server= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# permet de liberer le port apres un CTRL + C 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server.bind((host, port ))

print(f"Le serveur UDP en ecoute sur {port}\n")

while True:
    request , address = server.recvfrom(4196)

    print("Message client: ",request.decode("utf-8"))
    print("IP du client connecte :", address)
    server.sendto(b"I am the server", address)


request.close()
server.close()