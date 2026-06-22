# from sqlite3 import *
import sqlite3
myfile="EXO2.db"

# con=connect(":memory")
conn=sqlite3.connect(myfile)
cur=conn.cursor()
try:
    cur.execute("CREATE TABLE  exo1(name TEXT,age INTEGER ,)")
    conn.commit()
    print("la table est creee ...\n")

    # cur.execute("""SELECT * FROM exo1""")
    display= cur.fetchall()
except sqlite3.OperationalError:
    print("une erreur est survenu ")


finally:   
    cur.close()
    conn.close()