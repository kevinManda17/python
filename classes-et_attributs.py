#coding:utf-8

"""class Humain :
    def __init__(self,C_prenom="keven",C_age=18):
        print("creation d'un Humain !")
        self.prenom=C_prenom
        self.age=C_age

print("Lancement du programme...")

kevin=Humain("kevin", 20)

print("Prenom de Kevin: {}".format(kevin.prenom))
print("Age de kevin: {}".format(kevin.age))

kevin.prenom="thomas"
print("Prenom de kevin: {}".format(kevin.prenom))"""

#attributs de classe 

class Humain :
    Humains_crees=0
    def __init__(self,C_prenom="keven",C_age=18):
        print("creation d'un Humain !")
        self.prenom=C_prenom
        self.age=C_age
        Humain.Humains_crees+=1

print("Lancement du programme...")

kevin=Humain("kevin", 20)
print("Humian existants :{}".format(Humain.Humains_crees))

kvn=Humain("kvn", 20)
print("Humian existants :{}".format(Humain.Humains_crees))