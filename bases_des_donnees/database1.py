import sqlite3

my_file="ma_base.db"

my_connection= sqlite3.connect(my_file)
my_cursor=my_connection.cursor()
print(my_cursor)
print(my_connection)
print(type(my_cursor))
my_cursor.execute(" SELECT * FROM membres ")
i=1
for data in my_cursor:
    print(f"le numero {i} et ses informations{data} ")
    i+=1
    print()
print()
my_cursor.execute("SELECT * FROM membres ")
# cur=list(my_cursor)
print(f"l'adresse memoire du curseur :{my_cursor} et son type de donnees :{type(my_cursor)}")
print()
# print(f"la liste est : {cur} et ses autres element {type(cur)}")
print()
# print(cur)


data1=[(16,"kestia",1.57),(19,"keren",1.71),(10,"davina",1,30),(13,"Patricia",1.54),(5,"andrea",0.97)]
for i in data1 :
    print(i)
    for k in i :
        print(k)

andrea=(5,"andrea",0.97)
my_cursor.execute("INSERT INTO membres (age,nom ,taille) VALUES(?,?,?)",andrea)
my_connection.commit()
my_cursor.execute(" SELECT * FROM membres ")
i=1
for data in my_cursor:
    print(f"{data} ")
    i+=1
    print()
print("l'ajout a bien ete fait pour les noms dans data1")

my_cursor.execute("UPDATE membres SET nom='ANDREA' WHERE nom='andrea'")
my_connection.commit()
print("on a bien remplace le nom que vous avez desise remplacer !")
my_cursor.execute(" SELECT * FROM membres ")
i=1
for data in my_cursor:
    print(f"{data} ")
    i+=1
    print()
my_cursor.execute("delete from membres where nom='master'")
my_connection.commit()
my_cursor.execute(" SELECT * FROM membres ")

for data in my_cursor:
    print(f"{data} ")
    print()
my_cursor.close()
my_connection.close()