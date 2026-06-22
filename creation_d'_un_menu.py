import tkinter

def montre_apropos():
    about_window=tkinter.Toplevel(app)
    about_window.title("A propos")
    lb=tkinter.Label(about_window,text="bonjour")
    
    lb.pack()
     
# creation d'un menu 
app=tkinter.Tk()
app.geometry("680x480")
app.title("creation de menu")

# widgets
mainmenu=tkinter.Menu(app)


first_menu=tkinter.Menu(mainmenu,tearoff=0)
first_menu.add_command(label='option1')
first_menu.add_command(label='option2')
first_menu.add_command(label='quitter',command=app.quit)

second_menu=tkinter.Menu(mainmenu,tearoff=0)
second_menu.add_command(label="commande1")
second_menu.add_command(label="A propos", command=montre_apropos)

mainmenu.add_cascade(label="premier",menu=first_menu)
mainmenu.add_cascade(label="second",menu=second_menu)
# boucle principale
app.config(menu=mainmenu)
app.mainloop()