from sqlite3 import *

myfile="exo3.db"
conn=connect(myfile)
cur=conn.cursor()

cur.execute("""
select * from kvn

""")
