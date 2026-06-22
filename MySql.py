import mysql.connector as Mc

'@kevinManda' 
 
host = "localhost"
database= 'list'
user="root"
password= ''
try :
   
    conn = Mc.connect(host = "localhost",database= 'list',user="root",password= '')
    cursor = conn.cursor()
    req = 'SELECT * FROM fam'
    cursor.execute(req)
    
    _list = cursor.fetchall()

    for name in _list : 

        print(f"prenom :{name[1]} {name[2]} {name[3]}")

except Mc.Error as err:

    print(err)
finally :

    if (conn.is_connected()):
        cursor.close()
        conn.close()