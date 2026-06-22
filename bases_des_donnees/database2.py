#coding:utf-8
import sqlite3 

myfile="ma_base.db"
myconnection=sqlite3.connect(myfile)
mycursor=myconnection.cursor()

data1=[(16,"kestia",1.57),(19,"keren",1.71),(10,"davina",1,30),(13,"Patricia",1.54),(5,"andrea",0.97)]
for i in data1 :
    mycursor.executemany("INSERT INTO membres (age,nom,taille) VALUES(?,?,?)", data1)

myconnection.commit() 

print("les donnees ont bien ete ajouutees !")

mycursor.execute("SELECT * FROM MEMBRES ")
mycursor.close()
myconnection.close()