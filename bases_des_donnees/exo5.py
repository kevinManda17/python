import sqlite3

myfile="mybaseTuple.db"
con= sqlite3.connect(myfile)

cur=con.cursor()

data= {"name":"kevin", "age":20, "equipement": "PC GAMER "}
try :

    cur.execute("create table if not exists T_user(name text, age integer ,equipement text)")
    con.commit()

    cur.execute("insert into T_user(name, age, equipement) values(:name , :age , :equipement )", data )
    con.commit()

    cur.execute("select * from T_user ")
    print(F"les elements de la table: {cur.fetchall()}")
    id= cur.lastrowid

    print(f"dernier id: {id}")
    cur.execute("drop table t_user ")
    con.commit()

    cur.execute("select * from T_user ")

except sqlite3.OperationalError:

    print(F"la liste vide est : {cur.fetchall()} evidement ca retourne une erreur ,car la table a ete supprimee")
    
finally:
    con.close()
