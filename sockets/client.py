#coding:utf-8
import socket

def con_client():
    pass 

host , port =("127.0.0.1",5566)
# host , port =("localhost",5566) 
my_soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    my_soc.connect((host, port))
    print("Client connecte !")
    while True:
        text = input("(quit pour quitter) message: ")
        if text =="quit":
            break
        data= f"{text}"
        data=data.encode("utf-8")
        my_soc.sendall(data)

        turning_connected= True
except :
    print("Connexion au serveur echoue !")
finally:
    my_soc.close()
    