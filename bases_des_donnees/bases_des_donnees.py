#coding:utf-8
import sqlite3

connexion=sqlite3.connect("kvn_base.db")
cursor = connexion.cursor()


MonNomUtilisateur=("kevin",)

cursor.execute('SELECT * FROM kvn_utilisateurs WHERE Nom_utilisateur= ?',MonNomUtilisateur)
resultat=cursor.fetchone()[1]

print(f"Le nom d'utilisateur est :{resultat}")

connexion.close() 