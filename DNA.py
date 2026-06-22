n= int(input("entrez un nombre : "))
t=0 
l = []
for  i in range(0, n+1):
    if i % 2 == 0:
        t =t +i 
        l.append(t)
print(t) 
print(l)


n = int(input("entrez une valeur : "))
def fibonacci(t):
    if t<= 1 :
        return t
    else:
        return (fibonacci(t-1)+ fibonacci(t-2))
for i in range(0,n):
    print(fibonacci(i)) 


matrice = [
    [1,2],
    [3,4],
    [5,6],
]
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(matrice[i][j] , end=" ")
    print()



def nbpremier(n):
    if n <= 1 :
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0 :
            return False 
    return True
num= int(input("une valeur : "))
if nbpremier(num) :
    print(f"{num} est premier ")
else:
    print(f"{num} n'est premier ")