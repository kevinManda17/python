from tkinter import *


root = Tk()
# Creating label for widget 
myLabel1 = Label(root , text= "Hello Kevin ! " )
myLabel2 = Label(root , text= "thanks for using the app you will be  blessed  " )
myLabel3 = Label(root , text= "I put some texts in  " )


# Shoving it onto the screen 


myLabel1.grid(row= 0, column= 0)
myLabel2.grid(row= 1, column= 5)
myLabel3.grid(row= 1, column= 1)



root.mainloop()