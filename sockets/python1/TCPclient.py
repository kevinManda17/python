from socket import * 


host , port = ("127.0.0.1",9000)
s=socket(AF_INET, SOCK_STREAM)
s.connect((host ,port ))  # connect 
data= "bonjour"
s.send(data) # send request 
data = s.recv(10000)    # get response 
print("L'information a bien ete envoyee...")
s.close()
