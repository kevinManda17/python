import sqlite3

myfile="myBase.db"
con= sqlite3.connect(myfile)

cur=con.cursor()

cur.execute("select * from exo ")

print(cur.fetchall())

con.close()