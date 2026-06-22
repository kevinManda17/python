class A :
    def __init__(self , a ):
        self.donneeA = a

class B : 
    def __init__(self, b ):
        self.donneeB = b

class C (A, B):
    def __init__(self , a , b , c ):
        A.__init__(self,a)
        B.__init__(self,b)
        self.donneeC = c 


objA = A(1)
objB= B(2)
objC= C(3, 4, 5)

print(f" objA.donneeA: {objA.donneeA}")
print(f"objB.donneeB :{objB.donneeB}")
print(f" objC.donneeA :{objC.donneeA}")
print(f"objC.donneeB : {objC.donneeB}")
print(f"objC.donneeC : {objC.donneeC}")