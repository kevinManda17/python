import sqlite3
# from  sqlite3 import *


file_="ma_base.db"
connection_=sqlite3.connect(file_)
cursor_= connection_.cursor()

cursor_.execute("create table membres (age INTEGER, nom TEXT , taille REAL)")

cursor_.execute("insert into membres(age, nom, taille) values(21, 'kevin' ,1.73)")
cursor_.execute("insert into membres(age, nom, taille) values(21,'Master',1.77)")
cursor_.execute("insert into membres(age, nom, taille) values(21,'Entrepreneur',1.83)")

connection_.commit()

cursor_.close()
connection_.close()

print("L'ajout des informations a bien ete fait")
