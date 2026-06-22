# object oriented programming : -----)> OOP

class Mannifere():
    "classe parente: classe mannifere "
    caract1="il allaite ses petits ;"

class Carnivore(Mannifere):
    "une classe carnivore "
    caract2="il se nourit de la chair de ses proies ;"

class chien(Carnivore):
    "classe chien "
    caract3="son crie s'appelle aboiement ;"

mirza= chien()
print(mirza.caract1,mirza.caract2,mirza.caract3, )

mir=mirza.caract2="Son corp est couvert de poils"
print(mir)

fido=chien()
print(fido.caract2)