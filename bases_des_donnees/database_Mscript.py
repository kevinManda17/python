import sqlite3

myfile="musique.db"
basedonn=sqlite3.connect(myfile)
cur=basedonn.cursor()
while 1:
    print("Veuillez entrer votre requete SQL (ou <enter> pour terminer ):_")
    requete= input("Entre la requete: ")
    if requete =="":
        break 
    try :
        cur.execute(requete)
    except:
        print("*** requete SQL incorrecte ***")
    else:
        for enreg in cur :
            print(enreg)
        print()

choix= input("Confirmez-vous l'enregistrement de l'etat actuel (O/N) ?")
if choix =="o" or choix =="O":
    basedonn.commit()
    print("Une operation de votre choix  a ete faite !")
else :
    basedonn.close()