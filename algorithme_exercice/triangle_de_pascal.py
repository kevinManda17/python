# @kevin Manda 

# un triangle de pascal 

for n in range(10):
    for p in range(n+1):
        num = 1 
        den = 1
        for i in range(1, p+1 ):
            num = num*(n-i+1)
            den = den*i
        c=int( num/den) 
        print(c, end=' ')
    print()