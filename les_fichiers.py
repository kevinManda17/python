fic=open("textfile.txt","r")

with open("textfile.txt","w") as fic :
    ma_chaine="bonjour a tous j'espere que vous allez bien !"
    fic.write(ma_chaine)
    fic.write("\n")
    fic.write("comment etait ta journee ?")
if fic.closed:
    print("fichier ferme")
else:
    print("fichier ouvert")

class player:
    def __init__(self,name,level):
        self.name=name
        self.level=level
    def whoami(self):
        print("{} ({})".format(self.name, self.level))
p1=player("kevin",20)        
p1.whoami() 