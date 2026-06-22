import sqlite3

myfile="i.db"
# try:
con= sqlite3.connect(myfile)
cur=con.cursor()
cur.execute("""
CREATE TABLE if not exists temp_user(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE ,
                name TEXT ,
                point INTEGER 
)
""")
con.commit()
data=[]
data.append((1,"kevin",20))
cur.execute("insert into temp_user values(?,?,?)",data)
con.commit()
cur.execute("select  * from temp_user")
rows= cur.fetchall()
print(rows)
con.close()
# except sqlite3.OperationalError :
#     print(" Erreur: La table existe deja ")
# except Exception as e :
#     print("Erreur", e)
#     con.rollback()
#     # raise e 

# finally:
#  con.rollback()