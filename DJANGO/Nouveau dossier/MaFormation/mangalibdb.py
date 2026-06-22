import sqlite3 

myfile="maformation.db"

connection= sqlite3.connect(myfile)
cur= connection.cursor()

cur.execute("create table if not exists MANGALIB_k_book(id, title, quantity, author_id)")


# cur.execute("insert into MANGALIB_k_book(id , title , quantity , author_id ) values (1,'Naruto',136,2)")
# cur.execute("insert into MANGALIB_k_book(id , title , quantity , author_id ) values (2,'Dragon ball',342,1)")
# cur.execute("insert into MANGALIB_k_book(id , title , quantity , author_id ) values (3,'one piece' , 44, 3)")
# cur.execute("insert into MANGALIB_k_book(id , title , quantity , author_id ) values (4,'Death note',1,4)")
cur.execute("insert into MANGALIB_k_book(id, title , quantity , author_id) values(5,'Naruto shippuden',720,2)")
cur.execute("insert into MANGALIB_k_book(id, title , quantity , author_id) values(6,'Les insectes en moi',133,6)")
cur.execute("insert into MANGALIB_k_book(id, title , quantity , author_id) values(7,'Dr Slump',243,1)")
cur.execute("insert into MANGALIB_k_book(id, title , quantity , author_id) values(8,'Love Hina',200,7)")
cur.execute("insert into MANGALIB_k_book(id, title , quantity , author_id) values(9,'Negima! Le maitre magicien',199,7)")
cur.execute("insert into MANGALIB_k_book(id, title , quantity , author_id) values(10,'Fairy Tail',345,8)")
cur.execute("insert into MANGALIB_k_book(id, title , quantity , author_id) values(11,'Fullmetal Alchemist',156,9)")
cur.execute("insert into MANGALIB_k_book(id, title , quantity , author_id) values(12,'Rouge Bonbon',78, 10)")
cur.execute("insert into MANGALIB_k_book(id , title , quantity ,author_id) values(13,'A Silent Voice',234,11)")
connection.commit()

print("Tout a ete ajoute")

# cur.execute("drop table MANGALIB_k_book ")
# print("L'operation de suppression reussie")

connection.close()