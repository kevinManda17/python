class Humain():

    "class des humains"
    lieu_habitation="terre"
    def __init__(self,nom, age):
        self.nom=nom
        self.age=age

    def parler(self):
        print(f"{self.nom} a {self.age} ans")

    def changer_planete(cls,nouvelle_plante):
        Humain.lieu_habitation=nouvelle_plante
    changer_planete=classmethod(changer_planete)

#programme principal
h1=Humain("kevin",20)
h1.parler()
print("planete actuelle: {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")

print("planete actuelle: {}".format(Humain.lieu_habitation))