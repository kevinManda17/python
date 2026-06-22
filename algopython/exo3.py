class fact():

    """une classe factorielle quelle perte de temps !"""

    def __init__(self,n):
        self.n=n

    def facto(self,n,f):
         fact.__init__(self,n)
        #  n=input("calculons la factorielle: ")
         if n == 0:
            pass
            print(1)
         elif n==1 :
             print(1)
         else:
            f= 1
            for k in range(2,n+1):
                f=f*k
                # return f
            print(f)
 
factor=fact('')
factor.facto(n=int(input("calculons la factorielle: ")), f=int(input('Entrer F: ')))