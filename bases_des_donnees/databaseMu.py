import sqlite3 

myfile="musique.db"
con=sqlite3.connect(myfile)
cur=con.cursor()

cur.execute("create table if not exists compositeur (comp text , a_naiss text , a_mort )")
data=[]
data.append(("Mozart",1756,1791))
data.append(("Beethoven",1770,1827))
data.append(("Haendel",1685,1759))
data.append(("Schubert",1797,1828))
data.append(("Vivaldi",1678,1741))
data.append(("Monteverdi",1567,1643))
data.append(("Chopin",1810,1849))
data.append(("Bach",1685,1750))
data.append(("Shostakovich",1906,1975))
cur.executemany("insert into compositeur values(?,?,?)",data)
con.commit()

cur.execute("create table if not exists oeuvres(comp text , titre text, duree integer , interpr text  )")

data1= []
data1.append(("vivaldi","Les quatres saisons ",20,"T.Pinnock"))
data1.append(("Mozart","concerto piano N`12 ",25 ,"M.Perahia"))
data1.append(("Brahams","Concerto",40,"A.Grumiaux"))
data1.append(("Beethoven","Sonate 'au clair de lune' ",14,"W.Kempf"))
data1.append(("Beethoven","Sonate 'pathetique' ",17,"W.kempf"))
data1.append(("Schubert","Quitette 'la truite' ",39,"SE of London"))
data1.append(("Hayun","La creation ",109,"H.von Karajan"))
data1.append(("Chopin","Concerto piano N`1 ",42,"M.J. Pires "))
data1.append(("Bach","Toccata & fugue",9,"P.Burmester"))
data1.append(("beethoven","Concerto piano n`4",33,"M.Pollini"))
data1.append(("Mozart","Symphonie N`40",29,"F.Bruggen"))
data1.append(("Mozart","Concerto piano N`22",35,"S.Richter"))
data1.append(("Beethoven","Concerto N`3",37,"S.Richter"))
cur.executemany("insert into oeuvres values(?,?,?,?)",data1)
con.commit()

print("L'operation a ete un succes ...")
