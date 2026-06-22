from sqlite3 import *

base="myBase.db"
conn=connect(base)
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS exo(Nom TEXT,age INTEGER,taille REAL)")

print("Notre base a bien ete creee...\n")

cur.execute("insert into exo (nom, age , taille) values('kevin',20,1.73) ")
cur.execute("insert into exo (nom, age , taille) values('keren',18,1.70) ")
cur.execute("insert into exo (nom, age , taille) values('kestia',16,1.63) ")
cur.execute("insert into exo (nom, age , taille) values('patricia',13,1.60) ")
cur.execute("insert into exo (nom, age , taille) values('davina',10,1.35) ")
cur.execute("insert into exo (nom, age , taille) values('andrea',5,0.97) ")
cur.execute("insert into exo (nom, age , taille) values('jeremie',21,1.74) ")
cur.execute("insert into exo (nom, age , taille) values('Entrepreneur',20,1.73) ")

print("les donnees ont bien ete ajoutees !\n")
conn.commit()

cur.execute("SELECT * FROM exo ")
i=1
for data in cur:
    print(f"#id{i}: {data}")
    i+=1
# cur.execute("drop table exo")
# cur.execute("select * from exo ")
cur.close()
conn.close()