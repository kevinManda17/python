class Humain ():

    "on cree des humains "

    def __init__(self,nom,age):
        
        print("Creation d'un humain")
        self._nom=nom
        self._age=age

    def _getage(self):
        return self._age
    
    #property(<getter>, <setter>,<deleter>, <helper>)
    age=property(_getage)

#programme principal
h1=Humain("kevin",20)
print(h1.age)

