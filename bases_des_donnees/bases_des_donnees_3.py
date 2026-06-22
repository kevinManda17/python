#coding:utf-8
import sqlite3

try:
    con=sqlite3.connect("kvn_base.db")
    cur=con.cursor()
    req=cur.execute('SELECT * FROM kvn_utilisateurs')
    data = req.fetchall()
    for  row in data:
        print(f"#Id {row[0]}, nom: {row[1]}, level: {row[2]}")


except Exception as e:
    print("[ERREUR]",e)
    con.rollback()
finally:
    con.close()


