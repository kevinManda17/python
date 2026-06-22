lst=["bob","alice","charlie"]
def ajouter(l,nom,i):
    if 0 <=i <= len(l):
        lst.insert(i,nom)
    else :
        print("l'indice i n'est pas valide pour cette liste ")


print(f"{lst} avant l'ajout de la liste ")

ajouter(lst,"david",1)

print(f"{lst} apres l'ajout de la liste")