from tkinter import *


fenetre= Tk()


can=Canvas(fenetre,bg="white",height=300, width=300)
can.pack()

can.create_oval(10,60,290,240,fill="red",outline="red")
can.create_oval(150-10,150-10,150+10,150+10,fill="white",outline="white")


fenetre.mainloop()