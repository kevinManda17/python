import sqlite3 

myfile="myappend.db"
con=sqlite3.connect(myfile)
cur=con.cursor()
try:
    cur.execute("create table  if not exists Users2(Id INTEGER , Name TEXT, Point INTEGER  )")
    con.commit()
    # data= [(1,"Electronics",40),(2,"Electicite",35),(3,"Circuit Logique",32)]
    
    data=[]
    data.append((1,"Electronics",40))
    data.append((2,"Electricite",35))
    data.append((3,"Circuit Logique",32))
    cur.executemany("insert into Users2 values(?,?,?)",data)
    con.commit()
    id=2
    cur.execute(""" select id , name from Users2 where id= ?""",(id,))
    cur.execute("UPDATE Users2 SET point= ? where id= 3",(37,))
    con.commit()

    # manipulation deux 
    rows=cur.fetchone()
    print("l'operation a ete faite ...")
    # cur.execute("drop table Users2")
    # print("La table a bien ete supprimee !")

except TypeError as err:
    err="Nonetype, pas de type "
    print(F"l'erreur est :{err}")

con.close()