#coding:utf-8

class CompteBancaire():

    "creating account"

    def __init__(self,nom="dupont",solde=1000):

        self.nom=nom
        self.solde=solde

    def depot(self,b):

        self.b=b
        self.solde=self.solde+ self.b

    def retrait(self,a):

        self.a=a
        self.solde=self.solde+self.a
        
    def affiche(self):

        print(f"le solde de compte bancaire de {self.nom} est de {self.solde} dollars.")
        print()

compte1=CompteBancaire("kevin",1000000)
compte1.depot(5000)
compte1.retrait(1258)
compte1.affiche()

compte2=CompteBancaire("Manda",3750000)
compte2.depot(700000)
compte2.retrait(2500000)
compte2.affiche()
