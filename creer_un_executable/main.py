import  tkinter 
import appk

def open():
    appk.run()

app = tkinter.Tk()
app.title("Mon application")
app.geometry("300x100")

lb= tkinter.Label(app, text="Cliquer sur le bouton ...").pack()
bt = tkinter.Button(app, text="Hack tkinter", command= open ).pack()

app.mainloop()