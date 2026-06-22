#coding:utf-8

"""
c'est quoi une methode speciale: 
c'est une methode definie par python avec deux __ au debut et la fin

"""

class Lapin():
    def __init__(self, name , weight):
        self.name= name 
        self.weight = weight

    def hello(self):
        print("Hello !")

    def __repr__(self):
        return f"lapin {self.name} de {self.weight}Kg"

    def __eq__(self, other):
        if self.weight == other.weight:
            return True
        return False 
    
lp = Lapin("coco", 25)
lp2 = Lapin("Titi", 25)
# lp.hello()

print(lp)
print(lp2)

if lp == lp2 :
    print("Ce sont les memes ")
else :
    print("Ces lapins sont differents")

