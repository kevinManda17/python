host= "localhost"
port=46000

import socket , sys , threading
class ThreadClient(threading.Thread):
    """derivation d'un objet thread pour gerer la connexion avec un client 
       @KEVIN MANDA MUBENGA :-----> TOWARS SUCCESS !
    """
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection= connection

    def  run(self):
        name= self.getName()
        while 1:
            client_message=self.connection.recv(4196).decode("utf8")
            if not client_message or client_message.upper() == "FIN":
                break
            message="%s> %s" %(name,client_message)
            print(message)
            for key in conn_client :
                if key != name :
                    conn_client[key].sendall(message.encode("utf8"))
        self.connection.close()

        del conn_client[name]
        print("Client %s deconnecte." % name)

mysocket= socket,socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    mysocket.bind((host,))
except socket.error :
    print("La liaison du socket a l' adresse choisie a echoue ")
    sys.exit()
print("Serveur est en marche... ")
mysocket.listen(10)

conn_client={}
while 1:
    connected, address= mysocket.accept()
    th=ThreadClient(connected)
    th.start()
    it = th.getName()
    conn_client[it]= connected
    print("client %s connecte. , adresse IP %s , port %s ") %\
          (it, address[0], address[1])
    msg= "vous etes connecte. envoyer vos messages "
    connected.send(msg.encode("utf8"))
    