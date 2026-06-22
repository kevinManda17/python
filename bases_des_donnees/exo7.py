import sqlite3 

myfile="myappend.db"
con=sqlite3.connect(myfile)
cur=con.cursor()
try:
    cur.execute("create table  if not exists Users1(Id INTEGER , Name TEXT, Point INTEGER  )")
    con.commit()
    # data= [(1,"Electronics",40),(2,"Electicite",35),(3,"Circuit Logique",32)]
    data=[]
    data.append((1,"Electronics",40))
    data.append((2,"Electricite",35))
    data.append((3,"Circuit Logique",32))
    
    cur.executemany("insert into Users1 values(?,?,?)",data)
    cur.execute("""select  id , name , point from Users1""")
    
    # manipulation deux 
    rows=cur.fetchall()
    print(rows)
    for row in rows :
        print(F"{row[0]}, {row[1]}, {row[2]}\t")
        # print("{0}: {1}---{2}".format(row[0], row[1], row[2]))

except TypeError as err:
    err="Nonetype, pas de type "
    print(F"l'erreur est :{err}")

con.close()