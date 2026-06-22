class NombreComplexe():
    def __init__(self, r, i ):
        self.re = r
        self.im = i


    def __str__(self):
        if self.im >= 0 :
            return str(self.re) + '+' + str(self.im) + 'i'
        else :
            return f'{str(self.re)}{str(self.im)}i'
        

nc1 = NombreComplexe(6 , 3)



print(nc1)
