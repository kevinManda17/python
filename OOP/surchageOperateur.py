class NombreComplexe :

    def __init__ (self,r,i) :
        self.Re = r
        self.Im = i
    def __add__ (self, operandeDroite) :
        resultat = NombreComplexe(self.Re,self.Im)
        resultat.Re += operandeDroite.Re
        resultat.Im += operandeDroite.Im
        return resultat
    
    def __eq__(self , nc ):
        return self.Re == nc.Re and self.Im == nc.Im
    
    def __invert__(self):
        self.Im = -self.Im
        return self.Im

    def __str__(self):
        return f'{str(self.Re)}+{str(self.Im)}i'
    


nc1 = NombreComplexe(5,2)
nc2 = NombreComplexe(-1,1)
nc3 = nc1 + nc2 

print(nc3)


nc3 =NombreComplexe(8 , 3 )
nc4 = NombreComplexe(-3, 2)

estegal = (nc3 == nc4 )

print(estegal)

nc5 = NombreComplexe(5 , 2 )

print(nc5)
