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
