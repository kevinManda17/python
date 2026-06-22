import socket 

host="localhost"
port=4000
#create an INET, STREAMing socket 
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try :
    soc.connect((host,port))
    print("le client connecte !")
    while True :
        text=input('entrez message :')
        if text=='quit':
            break

        data=f"{text}"
        data=data.encode("utf8")
        soc.sendall(data)
except:
    print("la connexion echoue !")
finally:
    soc.close()