#coding:utf-8

class Humain:
    # classe qui definit un  humain

    def __init__(self,nom, age):
        self.nom=nom
        self.age= age
    def parler(self,message):
        print("{} a dit : {}".format(self.nom,message))

# programme principal
h1=Humain("kevin", 20)
h1.parler("bonjour a tous !")
h1.parler("comment allez-vous ?")