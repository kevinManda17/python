class Humain:
    """classe des humains"""
    lieu_habitation="terre"
    
    def __init__(self, nom, age):
        self.nom= nom 
        self.age= age

    def parler(self,message):
        print(f"{self.nom} a dit {message}")
    
    def changer_planete(cls, nouvelle_planete):
        Humain.lieu_habitation= nouvelle_planete
    
    changer_planete=classmethod(changer_planete)

h1=Humain("Kevin", 20)

h1.parler("Bonjour a tous !")

print(f"Plante ancienne : {Humain.lieu_habitation}")

Humain.changer_planete("mars")

print(f"Plante actuelle : {Humain.lieu_habitation}")