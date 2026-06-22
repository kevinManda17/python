#coding: utf-8


dico= {"prenom":"kevin","age":"20 ans"}

# print(dico["prenom"])

dico={"chien":"le meilleur ami de l'homme, c'est un mannifere"}
dico["chat"]="C'est un felin "
# print(dico)


valeur=dico.pop("chat")

# print(dico,"\n")

# print(valeur,"\n")

dico["chat"]="C'est un felin "
# print(dico,"\n")
del dico["chat"]
# print(dico)

dico["chat"]="C'est un felin "
#   verification dans un dictionaire 

if "chien" in dico:
    # print(bool("oui"))
    # print('oui')
    pass

else : 
    # print(bool("Non "))
    pass
    
for key in dico.keys() :
    # print(key)
    pass

for key in dico.values():
    # print(key)
    pass

for (k, v) in dico.items():
    print(f"Cle :{k} et valeur {v}")
    pass 

dico1= {}
dico2= dico.copy()
# print(dico2)
# print(dico1)
dico1= dico2.copy()
# print(dico1)

def uneFonction(**itm):
    print(itm)

uneFonction(p="123", r=123)

def uneAutreFonction(**args):
    print(args)

uneAutreFonction(k=12,)