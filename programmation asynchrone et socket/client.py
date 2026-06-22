#coding:utf-8 
import socket 

host , port = ("localhost",2020)

my_soc= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try : 
    my_soc.connect((host,port))
    print("Client connecte !")
    while True : 
        mes=input("Entrez  un message:  ")
        if mes == "stop".upper() or "stop".lower():
            break
        else :
            data=f"{mes}"
            data=data.encode("utf8")
            my_soc.sendall(data)

except:
    print("Connexion au serveur echoue ")

finally:
    my_soc.close()