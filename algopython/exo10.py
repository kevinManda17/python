lst=["bob","alice","charlie"]
print(f"la liste {lst}")
lst2=['argent',"or"]
print(f"le liste 2 {lst2}")
lst3=lst+lst2
print(f"la liste 3 {lst3}")

def ajouter(l,nom,i):
    if 0 <=i <= len(l):
        lst3.insert(i,nom)
        return(print(f"la liste 3 apres l'ajout {lst3}"))
    else :
        print("l'indice i n'est pas valide pour cette liste ")

def echanger(x,y):
    lst3[x],lst3[y]=lst3[y],lst3[x]
    return print(f"la liste 3 apres l'echange {lst3}")

ajouter(lst,"kevin",1)
echanger(0,3)

