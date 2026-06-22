#coding:utf-8
import sqlite3 

connexion= sqlite3.connect("kvn_base.db")
curseur=connexion.cursor()

Nouvel_utilisateur=(curseur.lastrowid, "keven", 23)
curseur.execute('INSERT INTO kvn_utilisateurs VALUES(?,?,?)', Nouvel_utilisateur)

connexion.commit()

print("Nouvel utilisateur ajoute !")

connexion.close()