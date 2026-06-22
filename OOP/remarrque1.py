class A :
    def afficher(self) :
        print('A')
class B :
    def afficher(self) :
        print('B')
class C (A,B) :
    def afficher(self) :
        print('C')
        
objA = A()
objB = B()
objC = C()

objA.afficher() # affiche A
objB.afficher() # affiche B
objC.afficher() # affiche C

A.afficher(objC) # affiche A
B.afficher(objC) # affiche B
C.afficher(objC) # affiche C