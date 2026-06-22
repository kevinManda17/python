import socket
class Myscoket():
    """demonstration class only coded for clarity, not effiency"""
   
    def __init__(self, sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else :
            self.sock =sock
        
    def connect(self, host, port):
        self.sock((host,port))

    def mysend(self, data):
        Tsent=0
        while Tsent < MSGLEN :
            sent = self.sock.sendall(data[Tsent])
            if sent == 0:
                raise RuntimeError("socket connection is broken ")
            Tsent= Tsent + sent 


    def myreceive(self):
        chunks=[]
        bytes_recd =0
        while bytes_recd <MSGLEN :
            chunk= self.sock.recv(min(MSGLEN- bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection is broken")
            chunks.append(chunk)
            bytes_recd= bytes_recd + len(chunk)
        return b''. join(chunks)
    
MSGLEN= Myscoket()