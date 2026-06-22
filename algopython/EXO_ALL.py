def verif(numero):
    pays=numero[:4]
    val="le numero de telephone est de "
    inval="le numero de telephone n'est pas de "
    if pays == "+243":
        if len(numero) == 13:
            print(val,"la rdc")
        else: 
            print(inval,"la rdc")
    elif pays =="+272":
        if len(numero)== 12:
            print(val,"l'afrique du sud")
        else:
            print(inval,"de l'afrique du sud")
    elif pays=="+332":
        if len(numero):
            print(val,"de la belgique ")
        else:
            print(inval,"de la belgique") 
    elif pays =="+234":
        if len(numero):
            print(val,"du nigeria")
        else:
            print(f"{inval} du nigeria")
    else:
        print("L numero n'est pas pris en charge ") 

verif(input("Entrez votre numero: "))

print("---------------------------------------UN AUTRE EXERCICE------------------------------------")
password="mot_de_passe_exemple"

max_tries=3
tries=0

while tries < max_tries:
    user_input=input("Entrez le mot de passe: ")
    if user_input ==password:
        print("le mot de passe est valide ")
        break 
    else :
        print(f"le mot de passe n'est pas valide. il vous reste{tries} d'essais ")
        tries +=1
    if tries == max_tries:
        print("nombre maximal d'essais atteint. veuillez reessayer plutard !")

print("---------------------------------------UN AUTRE EXERCICE------------------------------------")

def facto(n):
    #  fact.__init__(self,n)
    # n=input("calculons la factorielle: ")
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
        print(f"{f} est la factorielle de {n}")

facto(n=int(input("calculons la factorielle: ")))     

# factor=fact("")
# factor.facto(n=int(input("calculons la factorielle: ")))

class fact():

    """une classe factorielle quelle perte de temps !"""
    
    def __init__(self,n):
        self.n=n

    def facto(self,n):
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
 
factor=fact(int(""))
factor.facto(n=int(input("calculons la factorielle: ")))

print("--------------------------------------- UN AUTRE EXERCICE ------------------------------------")

i= 0
N=int(input("Entrez un nombre: "))
while i< 10:
    N=N+1
    # N=n+1
    i +=1
    print(f"les 10 nombres suivant sont:{N}")

    
print("---------------------------------------UN AUTRE EXERCICE------------------------------------")
