#coding: utf-8

import socket 

host , port = ("localhost", 2020)

my_soc= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_soc.bind((host, port ))
print("Le serveur a ete demarre ...")

while True :
    my_soc.listen(10)
    conn , address = my_soc.accept()
    print("Le serveur est en ecoute ...")
    
    data=conn.recv(32768)
    data.decode("utf8")
    print(data)
conn.close()
my_soc.close()