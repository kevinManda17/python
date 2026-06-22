# coding:utf-8
# learn OOP:------)> object oriented programming

class Domino():
    
    """definition domino's class""" 
    
    def __init__(self, val_def=0, val_def1=0):
        self.a=val_def1
        self.b= val_def

    def affiche_point(self):
        print("Les points sont:","face A:",self.a,"face B:",self.b)
    
    def valeur(self,):
       
        return self.a+self.b
        


d1=Domino(2,6)
d2= Domino(4,3)
d1.affiche_point()
d2.affiche_point()
d1.valeur()
d2.valeur()
print("Le total des points: ",d1.valeur()+d2.valeur())

# liste_Domino=[]
# for i in range(7):
#     liste_Domino.append(Domino(6,i))
# print(liste_Domino[3])