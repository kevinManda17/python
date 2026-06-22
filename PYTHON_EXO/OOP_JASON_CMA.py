#coding: utf-8

class Humain():

    "classe des etres humains"
    
    def __init__(self,c_prenom='Kevin',c_age=20):
        print(f"Creation d'un humain...{self.prenom}")
        self.prenom=c_prenom
        self.age= c_age

print("Lancement du programme principal !")
    
h1=Humain("kakashi",33)

print(f"l'age de {h1.prenom} est {h1.age}")

h2=Humain("naturo",19) 
print(f"l'age de {h2.prenom} est {h2.age}")
