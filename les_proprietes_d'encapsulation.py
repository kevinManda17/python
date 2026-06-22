#coding:utf-8

class Humain:

    def __init__(self,nom,age):
        self.nom=nom
        self._age=age 

    def _getage(self):
        # print("recuperation interdit")
        try:
            return self._age   
        except AttributeError:
            print("l'age n'existe pas ") 
    def _setage(self, nouvel_age):
        if nouvel_age<=0:
            self._age=0
        else :
            self._age= nouvel_age
    def _delage(self):
        del self._age

    # property(<getter> ,<setter>,<deleter>, <helper>)
    age= property(_getage,_setage,_delage,"je suis l'age d'un Humain")
# programme principale 
h1= Humain("kevin",20)
h1._getage()


help(Humain)
help(Humain.age)