class Nombre :

    def __init__(self,n):
        self.nombreReel = n
    
    def __str__(self):
        return f'Nombre reel  {str(self.nombreReel)}'
    
class NombreComplexe(Nombre):
    def __init__ (self, re , im ):
        super().__init__(re)
        self.nombreImaginaire = im

        