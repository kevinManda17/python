kev_electronics=['keven',"kevin", "manda","mubenga"]
# pour verifier si les noms suivants sont dans la liste
verif_k="kestia" in kev_electronics
verif_kevin="kevin" in kev_electronics
verif_manda="manda" in kev_electronics
verif_keren="keren" in kev_electronics
print("kestia",verif_k)
print('manda',verif_manda)
print("keren",verif_keren)
print("kevin",verif_kevin)

# pour la taille de la liste 
taille_de_liste=len(kev_electronics)
print("la taille de la liste est de: ",taille_de_liste)
# pour ajouter un nom a la liste 
kev_electronics.append("carine")
print(kev_electronics)
# pour inserer un etudiant dans la liste 
kev_electronics.insert(0,"patricia")
print(kev_electronics)
# pour changer un element de la liste
kev_electronics[1]="kev_electrionics"
print(kev_electronics)
# pour reecrire la taille de la liste 
taille_de_liste=len(kev_electronics)
print("la taille de la liste est de: ",taille_de_liste)