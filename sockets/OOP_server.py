import socket

class Server_k():
    host ="localhost"
    port= 8080 
    def __init__(self,socke=None):
        if socke is None:
            self.sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.socke=socke
    def connecte():
        pass 