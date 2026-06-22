import sqlite3

myfile="myappend.db"
con= sqlite3.connect(myfile)

cur=con.cursor()

cur.execute("create table if not exists users(name text, point integer)")


users=[]
users.append(("olivier",20))
users.append(('kevin', 21))
users.append(("franck",14))
cur.executemany("insert into users(name, point ) values(?,?)",users) 

con.commit()

print(F"La liste a bien ete ajoutee ")
cur.execute("select * from users ")
rows=cur.fetchall()
id=1
# for row in cur.fetchall():
    # print(F"#id:{id}  ---> {row[0]} ")
    # pass
    # id +=1
for row in rows:
    # pass
    print(F"les elements de la liste {row}")
    for i in  row :

        print(F"Le premier de la table  {row[0]} ")
        print(F"\n Le deuxieme de la table{row[1]} ")
        print(F"\n Le troisieme de la table  {row[1]}")
        print(F"les elements sont choisis  par colonne ")      

con.close()  