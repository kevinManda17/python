# #coding:utf-8

# class Vehicule:
#     def __init__(self,nom_vehicule,quantite_essence):
#         self.nom= nom_vehicule
#         self.essence=quantite_essence

#     def se_deplacer(self):
#         # return self.nom 
#         # print("le vehicule {} se deplace...".format(self.nom))
#         print("je roule ...")
# class Voiture(Vehicule):
#     def __init__(self,nom_voiture, essence,puissance):
#         Vehicule.__init__(self,nom_voiture,essence)
#         self.puissance=puissance 

# class voitureSport(Voiture):
#     print()
# class Avion(Vehicule):
#     def __init__(self,nom,essence,marchandise):
#         Vehicule.__init__(self,nom,essence)
#         self.marchandise =marchandise 
#     def se_deplacer(self):
#         print("je survole les airs ...")
# # programme principale 
# voiture1=Voiture("toyata supra",90,420)
# voiture1.se_deplacer()
# print(voiture1.puissance,"CH")

# av1=Avion("f22 raptor",2400,"Missiles")
# av1.se_deplacer()


class Animal:
    def __init__(self,nom):
        self.nom=nom
    def manger(self):
        print(self.nom, " mange...")

class Reptile(Animal):
    def __init__(self,nom, regime_alimentaire):
        Animal.__init__(self, nom)
        self.regime_alimentaire=regime_alimentaire
    def manger(self):
        print("Le reptile mange...")

#code principal 

lezard=Reptile("lezard","grenouilles")
lezard.manger()