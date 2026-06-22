import sqlite3 

myfile="mangalib.db"

connection= sqlite3.connect(myfile)
cur= connection.cursor()

cur.execute("insert into mangalib_author(id, name ) values(1,'AKIRA TORIYAMA')")
cur.execute("insert into mangalib_author(id, name ) values(2,'MASACHI KICHIMOTO')")
cur.execute("insert into mangalib_author(id, name ) values(3,'ELCHIRO ODA ')")
cur.execute("insert into mangalib_author(id, name ) values(4,'TSUGUMI OHBA')")

# connection.commit()

# cur.execute("insert into mangalib_book(id , title , quatity , author_id ) values (1,'Naruto',6,2)")
# cur.execute("insert into mangalib_book(id , title , quatity , author_id ) values (2,'Dragon ball',34,1)")
# cur.execute("insert into mangalib_book(id , title , quatity , author_id ) values (3,'one piece' , 44, 3)")
# cur.execute("insert into mangalib_book(id , title , quatity , author_id ) values (4,'Death note',1,4)")

connection.commit()

print("Tout a ete ajoute")
connection.close()