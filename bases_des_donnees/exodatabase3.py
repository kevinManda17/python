from sqlite3 import *

myfile="EXO1.db"

# con=connect(":memory")
con=connect(myfile)
cur=con.cursor()
try:
    cur.execute("CREATE TABLE  exo1(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT,age INTEGER ,)")
    con.commit()
    print("la table est creee ...\n")

    cur.execute("""SELECT * FROM exo1""")
    display= cur.fetchall()
except OperationalError:
    print("une erreur est survenu ")


finally:   
    cur.close()
    con.close()