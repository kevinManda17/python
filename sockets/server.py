#coding:utf-8
import socket

host, port =("localhost", 5566)

socke= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socke.bind((host, port ))

print("Le serveur est demarre  ")

while True :
    socke.listen(5)
    conn , address=socke.accept()
    print("En ecoute...", f"client {conn} , address:{ address}")
    data = conn.recv(4196)
    data= data.decode("utf-8")
    print(data)
    # conn.close()

    # turning_on=True
    # while turning_on == True:
    #     socke.listen(10)
    #     conn , address=socke.accept()
    #     # print("En ecoute...", f"client {conn} , address:{ address}")
       
    #     # conn.close()
    #     # text=input("je maintiens notre connexion")
    #     print("En ecoute du client ...")
    #     data = conn.recv(4196)
    #     data= data.decode("utf-8")
    #     print(data)
    # print(conn)
    conn.close()
   
socke.close()