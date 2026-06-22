class Vehicule: 
    def __init__(self):
        print("Initialisation d'un véhicule")
        self.__vitesse = 0
        self.est_allume= False
        print(f"Vitesse: {self.__vitesse} km/h")

    def demarrer(self):
        self.est_allume = True
        print("Le véhicule démarre")

    def get_vitesse(self):
        return self.__vitesse
    
    def set_vitesse(self, vitesse):
        self.__vitesse = vitesse



class VehiculeTerrestre(Vehicule):
    def rouler(self):
        if self.est_allume:
            print("Le véhicule roule")
        else:
            print("Impossible, le véhicule est éteint")
        print(f"Vitesse: {self.get_vitesse()} km/h")

class VehiculeAerien(Vehicule):
    def decoller(self):
        if self.est_allume:
            print("Le véhicule décolle")
        else:
            print("Impossible, le véhicule est éteint")
        print(f"Vitesse: {self.get_vitesse()} km/h")


v1 =Vehicule()
v2 =VehiculeTerrestre()
v3 =VehiculeAerien()

