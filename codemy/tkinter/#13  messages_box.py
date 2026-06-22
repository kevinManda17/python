from tkinter import *
from tkinter import messagebox  


app = Tk()
app.geometry("300x300")
app.title("Messages boxes with tkinter ")
app.iconbitmap("img/lorem.ico")

# see some different of show messages on the screen 

    # showinfo , showwarning , showerror , askquestion , askcancel , askyesno

# define some  fuctions here 
def popup():
    response = messagebox.askquestion("You clicked on the button ", " Hello kevin Manda ")
    if response  == "yes":
        Label(app , text = f"You clicked {"yes".upper()}" , ).pack()
    else : 
        Label(app , text = f"You clicked {"no".upper()} " , ).pack()




Button(app , text = "Popup" , command = popup ).pack()


# loop for app 
app.mainloop() 
