#coding:utf-8

class Voiture():

    def __init__(self,marque="ford",couleur="rouges",pilote="personne", vitesse=0):
        
        self.marque=marque
        self.couleur=couleur
        self.pilote=pilote
        self.vitesse=vitesse

    def choix_conducteur(nom):
        nom=input("entrez un nom:")
        print(f"le conducteur est {nom}")

    def  acceleration(self,taux,duree):
        self.nom=""
        self.vitesse=taux*duree
        if self.nom == "personne":
            print("acceleration interdite !")
            pass
        else:
            print(f"la vitesse est : {self.vitesse} m/s")
            pass
    def affiche_tout(self,):
        Voiture.__init__(self,marque="ford",couleur="rouges",pilote="personne", vitesse=0)


a1=Voiture("peugot","bleur")
a2=Voiture(couleur="verte")
a3=Voiture("mercedes")

a1.choix_conducteur()
a2.choix_conducteur()
a2.acceleration(1.8,12)
a3.acceleration(1.9,11)
a2.affiche_tout()

print("------------------------------------------------ | Pas encore reussi !|----------------------------------------------")