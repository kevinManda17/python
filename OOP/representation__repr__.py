class NombreComplexe():
    def __init__(self, r, i ):
        self.re = r
        self.im = i


    def __repr__(self):
        if self.im > 0 :
            return str(self.re) + '+' + str(self.im) + 'i'
        else :
            return f'{str(self.re)}{str(self.im)}i'
        

nc1 = NombreComplexe(6 , 3)
nc2 = NombreComplexe(3, -2)


print(nc1)
print(nc2)