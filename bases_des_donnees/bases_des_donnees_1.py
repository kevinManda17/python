#coding:utf-8
import sqlite3

connection=sqlite3.connect("base1.db")
cursor=connection.cursor()

my_username=("kevin",)
cursor.execute("SELECT * FROM user1 WHERE UserName= ?",my_username)

print(cursor.fetchone())

connection.close()