import socket 

host , port = ("", 3000)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("", 3000))
print(f"Le serveur demarre sur le port {port}")
server.listen()

while True :
    client, infoClient =server.accept()
    request = client.recv(4196)
    print(request.decode("utf-8"))
    print("IP client connecte :",socket.gethostbyname(socket.gethostname()))

client.close()