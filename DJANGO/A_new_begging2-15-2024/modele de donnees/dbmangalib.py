import sqlite3 

myfile="manga.sqlite3"

connection= sqlite3.connect(myfile)
cur= connection.cursor()

cur.execute("create table if not exists manga_author(id, name )")

cur.execute("insert into manga_author(id, name ) values(1,'Akira toriyama')")
cur.execute("insert into manga_author(id, name ) values(2,' Massashi Kishimoto')")
cur.execute("insert into manga_author(id, name ) values(3,'Elchiro Oda ')")
cur.execute("insert into manga_author(id, name ) values(4,'Tsugumi Ohba')")
cur.execute("insert into manga_author(id, name) values(5,'Massashi Kishimoto')")
cur.execute("insert into manga_author(id, name) values(6,'Akino Kondoh')")
cur.execute("insert into manga_author(id, name) values(7,'Ken Akamatsu')")
cur.execute("insert into manga_author(id, name) values(8,'Hiro Mashima')")
cur.execute("insert into manga_author(id, name) values(9,'Hiromu Arakawa')")
cur.execute("insert into manga_author(id, name) values(10,'Cathy cassidy')")
cur.execute("insert into manga_author(id, name) values(11,'Yoshitoki Oima')")


connection.commit()

print("Tout a ete ajoute")

# cur.execute("drop table MANGALIB_k_author ")
# print("Le processus de suppression fait ...")

connection.close()

# cur.execute("""
#             insert into manga_author(id , name,)
#             values
#             (1,'Akira toriyama')
#             (2,' Massashi Kishimoto')
#             (3,'Elchiro Oda ')
#             (4,'Tsugumi Ohba')
#             (5,'Massashi Kishimoto')
#             (6,'Akino Kondoh')
#             (7,'Ken Akamatsu')
#             (8,'Hiro Mashima')
#             (9,'Hiromu Arakawa')
#             (10,'Cathy cassidy')
#             (11,'Yoshitoki Oima')")

# """)


# connection.commit()
# connection.close()

