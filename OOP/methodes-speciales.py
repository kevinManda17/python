class NombreComplexe1():
    def __init__(self):
        self.re = 0 
        self.im = 0

nc = NombreComplexe1()
# -------------------------------------------------
class NomberComplexe2():
    def __init__(self, r , i ):
        self.re = r 
        self.im= i 

nc1 = NomberComplexe2( 5, 4)

nc1.texte = "Je Suis Un Nombre Complexe "

print(nc1.texte)

# ---------------------------------------------------------

class NombreComplexe():
    nbComplexesCrees = 0
    def __init__(self ):
        self.Re = 0
        self.Im = 0 
        NombreComplexe.nbComplexesCrees +=1 
    
    def afficheNbComplexe(cls):
        print(NombreComplexe.nbComplexesCrees)
    afficheNbComplexe =classmethod(afficheNbComplexe)


NombreComplexe.afficheNbComplexe()

nc1 = NombreComplexe()
NombreComplexe.afficheNbComplexe()

nc2 = NombreComplexe()
NombreComplexe.afficheNbComplexe()