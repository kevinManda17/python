import math 

class SymetriqueAxial:
    def __init__(self, parama, paramb):
        self.a = parama
        self.b = paramb

class Forme:
    def __init__(self, x, y):
        self.posX = x
        self.posY = y

    def __str__(self):
        return f"{str(self.posX) } {str(self.posY)}"

class Trapeze(Forme):
    def __init__(self, x, y, long, larg, haut):
        Forme.__init__(self, x, y)
        self.hauteur = haut
        self.longeur = long
        self.largeur = larg
    def aire(self):
        return (self.longeur + self.largeur) *self.hauteur / 2.0
    
class Parallelogramme(Trapeze):
    def __init__(self, x, y, long, haut):
        Trapeze.__init__(self, x, y, long, long, haut)

class Rectangle(Parallelogramme, SymetriqueAxial):
    def __init__(self, x, y, long, larg):
        Parallelogramme.__init__(self, x, y, long ,larg)
        SymetriqueAxial.__init__(self, 0, y)



class Carre(Rectangle):
    def __init__(self, x, y, cote):
        Rectangle.__init__(self, x, y, cote, cote)

class Triangle(Forme):
    def __init__(self, x, y, h, b):
        Forme.__init__(self, x, y)
        self.hauteur = h
        self.base = b
    def aire(self):
        return (self.hauteur * self.base) / 2.0
    
class TriangleEquilateral(Triangle, SymetriqueAxial):
    def __init__(self, x, y, cote):
        Triangle.__init__(self, x, y, math.sqrt(3) * 
        cote / 2.0, cote)
        SymetriqueAxial.__init__(self, 0, y)

class Cercle(Forme, SymetriqueAxial):
    def __init__(self, x, y, r):
        Forme.__init__(self, x, y)
        self.radius = r
        SymetriqueAxial.__init__(self, 0, y)
        def aire(self):
            return math.pi * self.radius * self.radius
class Point(Cercle):
    def __init__(self, x, y):
        Cercle.__init__(self, x, y, 0)


f = Forme(2, 4)
print(f)