class Nombre :

    def __init__(self,n):
        self.nombreReel = n
    
    def __str__(self):
        return f'Nombre reel  {str(self.nombreReel)}'
    
class NombreComplexe(Nombre):
    def __init__(self, re , im ):
        Nombre.__init__(self ,  re )
        self.nombreImaginaire = im 

    def __str__(self):
        return f"Partie Reelle : {str(self.nombreReel)} + Partie Imaginaire : {str(self.nombreImaginaire)}" 
    

n = Nombre(5)
nc = NombreComplexe(4, 9)

print(n)
print(nc)


print(issubclass(Nombre , NombreComplexe))

print(isinstance(nc  , NombreComplexe))
