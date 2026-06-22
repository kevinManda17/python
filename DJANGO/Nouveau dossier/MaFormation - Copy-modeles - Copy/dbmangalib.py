import sqlite3 

myfile="maformation.db"

connection= sqlite3.connect(myfile)
cur= connection.cursor()

cur.execute("create table if not exists MANGALIB_k_author(id, name )")

# cur.execute("insert into MANGALIB_k_author(id, name ) values(1,'Akira toriyama')")
# cur.execute("insert into MANGALIB_k_author(id, name ) values(2,' Massashi Kishimoto')")
# cur.execute("insert into MANGALIB_k_author(id, name ) values(3,'Elchiro Oda ')")
# cur.execute("insert into MANGALIB_k_author(id, name ) values(4,'Tsugumi Ohba')")
cur.execute("insert into MANGALIB_k_author(id, name) values(5,'Massashi Kishimoto')")
cur.execute("insert into MANGALIB_k_author(id, name) values(6,'Akino Kondoh')")
cur.execute("insert into MANGALIB_k_author(id, name) values(7,'Ken Akamatsu')")
cur.execute("insert into MANGALIB_k_author(id, name) values(8,'Hiro Mashima')")
cur.execute("insert into MANGALIB_k_author(id, name) values(9,'Hiromu Arakawa')")
cur.execute("insert into MANGALIB_k_author(id, name) values(10,'Cathy cassidy')")
cur.execute("insert into MANGALIB_k_author(id, name) values(11,'Yoshitoki Oima')")


connection.commit()

print("Tout a ete ajoute")

# cur.execute("drop table MANGALIB_k_author ")
# print("Le processus de suppression fait ...")

connection.close()