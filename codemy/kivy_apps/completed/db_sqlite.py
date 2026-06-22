from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp
import sqlite3


#set the app size 
Window.size = (700, 500)

class MainApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        #create Database or connect To one 
        conn=sqlite3.connect("db_sqlite.db")
        cur = conn.cursor()

        #create the table
        cur.execute("""
                CREATE TABLE if not exists customers(name text )

            """)
        
        #commit our changes 
        conn.commit()

        #close our connection 
        conn.close()
        return Builder.load_file("db_sqlite.kv")

    def submit(self):

        #create Database or connect To one 
        conn=sqlite3.connect("completed/db_sqlite.db")

        cur = conn.cursor()

        #add A record
        cur.execute("INSERT INTO customers VALUES (:first)",{'first': self.root.ids.word_input.text, })

        #Add a little message
        self.root.ids.word_label.text =F"{self.root.ids.word_input.text}"

        #clear the input box 
        self.root.ids.word_input.text = ""

        #commit our changes 
        conn.commit()

        #close our connection 
        conn.close()

    def show_records(self):
         #create Database or connect To one 
        conn=sqlite3.connect("completed/db_sqlite.db")
        cur = conn.cursor()

        #Grab records from database 
        cur.execute("SELECT * FROM customers")
        records = cur.fetchall()

        word = ''
        #Loop thru records
        for record in records: 
            word =f"{word}\n{record[0]}"
            self.root.ids.word_label.text= F"{word}"
        
        #commit our changes 
        conn.commit()

        #close our connection 
        conn.close()

MainApp().run()

