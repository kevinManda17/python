import socket 
import os 
import _thread

serverSocket = None 
host = "127.0.0.1"
port = 10000 
Clients=[]
nbclients=0
numclient = None

def main():
    global nbclients
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    try:
        serverSocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    finally:
        print("Wainting for a connection...")
        serverSocket.listen(10)
    while True :
        client ,address = serverSocket.accept()
        print(f"Connecetd to : {address[0]} : {str(address[1])}")
        client.send(str.encode(str(nbclients)))
        Clients.append(client)
        print(f"Liste clients : {Clients}")
        start_new_thread(threaded_client, (client))
        nbclients +=1


def threaded_client(connection):
    global  nbclients
    print(f"connection : {connection}")
    while True : 
        data= connection.recv(4196)
        reply ="\n>>" + data.decode("utf-8") + "\n"
        for client in Clients : 
            client.sendall(str.encode(reply))

        if data == "quit ":
            numclient = int(connection.recv(4196))
            Clients[numclient].close()
            Clients.pop(numclient)
            nbclients -= 1

if __name__ == "__main__":
    main()