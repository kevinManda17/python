#coding: utf-8

import socket 

host='localhost'
port= 8000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc:
    soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    soc.bind((host,port))
    soc.listen(10)
    while True : 
        conn , address=soc.accept()
        print("le serveur est en marche !")
        with conn :
            buff = conn.recv(2048)
            message= buff.decode("utf-8")
            conn.sendall(f" Message: {message}".encode('utf-8'))
