from socket import *
host , port = ("localhost", 9000)

s= socket(AF_INET, SOCK_STREAM)
s.bind((host,port ))
s.listen(10)
print("Le serveur lance")
data="Bonjour"
while True :
    conn, addr =s.accept()
    print(f"Received connection from {addr}")
    # conn.send("Hello %s\n" % addr[0])
    conn.send(data)

    conn.close()

s.close()