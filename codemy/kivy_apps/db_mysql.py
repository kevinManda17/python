from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp
import mysql.connector as Mc


#set the app size 
Window.size = (500, 500)

class MainApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # define a database stuff 
        mydb = Mc.connect(
            host = "localhost",
            user= "root",
            passwd ="password123",
            database ="second_db"

        )
        cur = mydb.cursor()
        #create database
        cur.execute(
            "CREATE DATABASE IF NOT EXISTS second_db"
        )
        cur.execute("SHOW DATABASES ")

        #check to see if database was created 
        for db in cur :
            print(db)
            
        # #create the table
        cur.execute("""
                CREATE TABLE if not exists customers(name VARCHAR(50) )

            """)
        
        #check to see if table created 
        cur.execute("SELECT * FROM customers ")
        print(cur.description)
        #commit our changes 
        # mydb.commit()

        # #close our mydbection 
        # mydb.close()
        return Builder.load_file("db_mysql.kv")

    def submit(self):

        #create Database or mydbect To one 
        mydb = Mc.connect(
            host = "localhost",
            user= "root",
            passwd ="password123"

        )

        cur = mydb.cursor()

        #add A record
        cur.execute("INSERT INTO customers VALUES (:first)",{'first': self.root.ids.word_input.text, })

        #Add a little message
        self.root.ids.word_label.text =F"{self.root.ids.word_input.text}"

        #clear the input box 
        self.root.ids.word_input.text = ""

        #commit our changes 
        mydb.commit()

        #close 
        mydb.close()

    def show_records(self):

        # mydb=sqlite3.mydbect("completed/db_sqlite.db")
        mydb = Mc.connect(
            host = "localhost",
            user= "root",
            passwd ="password123"

         )
        cur = mydb.cursor()

        #Grab records from database 
        cur.execute("SELECT * FROM customers")
        records = cur.fetchall()

        word = ''
        #Loop thru records
        for record in records: 
            word =f"{word}\n{record[0]}"
            self.root.ids.word_label.text= F"{word}"
        
        #commit our changes 
        mydb.commit()

        #close our mydbection 
        mydb.close()

MainApp().run()

