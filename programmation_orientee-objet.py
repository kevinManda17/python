#coding:utf-8

class Humain :
    def __init__(self,C_prenom="kevin",C_age=18):
        print("creation d'un Humain !")
        self.prenom=C_prenom
        self.age=C_age

print("Lancement du programme...")

kevin=Humain("kevin", 20)

print("Prenom de Kevin: {}".format(kevin.prenom))
print("Age de kevin: {}".format(kevin.age))
kvn=Humain("kvn",19) 
print("Prenom de Kvn: {}".format(kvn.prenom))
print("Age de kvn: {}".format(kvn.age))