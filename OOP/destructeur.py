class NombreComplexe():

    def __init__(self):
        self.re = 0
        self.im= 0 

    def __str__(self):
        return f"{self.re} {self.im} "

    def __del__(self ):
        if self.re and self.im :   
            print("Le nombre a ete detruit ")
        else : 
            # print("Le nombre n'a pas ete detruit ")
            pass

nc1 = NombreComplexe()
print(nc1 )

# print(nc1.__del__)

print(nc1)