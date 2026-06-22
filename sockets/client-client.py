host="127.0.0.1"
port= 46000

import socket, sys , threading

class ThreadReception(threading.Thread):
    """objet thread gerant la reception des messages  """
    def __init__(self,connection):
        threading.Thread.__init__(self)
        self.connection= connection

    def run(self):
        while 1:
            got_message= self.connection.recv(4196).decode("utf8")
            print("*"+ got_message + "*")
            if not got_message or got_message.upper()== "FIN":
                break 
        th_E._stop()
        print("CLient arrete. connexion interrompue")
        self.connection.close()

class ThreadEmission(threading.Thread):
    """objet thread gerant l'emission des messsages"""
    def __init__(self,connection):
        threading.Thread.__init__(self)
        self.connection= connection

    def run(self):
        while 1:
            sent_message=input("votre messsage: ")
            self.connection.send(sent_message.encode("utf8"))

connection= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    connection.connect((host, port ))
except socket.error:
    print("La connexion a echoue.")
    sys.exit()
print("Connexion etablie avec le serveur ")

th_E=ThreadEmission(connection)
th_R=ThreadReception(connection)
th_E.start()
th_R.start()



