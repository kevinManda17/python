#coding:utf-8

#classe mere 
class Vehicule():

    def __init__(self,nom_vehicule,quatite_essence ):
        self.nom=nom_vehicule
        self.essence= quatite_essence 

    def se_deplacer(self):
        print(f"Le vehicule {self.nom} se deplace ...")


class Voiture(Vehicule):

    def __init__(self,nom_voiture,essence, puissance):
        Vehicule.__init__(self,nom_voiture,essence)
        self.puissance=puissance

    def se_deplacer(self):
        print("Je roule ...")

class Avion(Vehicule):

    def __inti__(self,nom,essence, marchandise):
        Vehicule.__init__(self, nom, essence, marchandise)
        self.marchandise=marchandise

    def se_deplacer(self):
        print("Je survole les airs ...")

#programme principal

voiture1= Voiture("Ford Explorer",90,420)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")