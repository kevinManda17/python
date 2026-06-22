import tkinter 

# creation et parametre de la fenetre 
app=tkinter.Tk()
app.geometry("640x480")
app.title("positionnement widget")

# widgets
# mainframe=tkinter.LabelFrame(app, text="cadre-nomme", width=300, height=200, borderwidth=1)
# mainframe.pack()

# label=tkinter.Label(app, text='le titre')
# ent=tkinter.Entry(app)
btn=tkinter.Button(app, text='bienvenu')


# label.pack()
# ent.pack()
# btn.pack(ipadx=100, ipady=50)

# label.grid(sticky="ne")
# ent.grid(row=2, column=4)
# btn.grid(rowspan=2, columnspan=3)

btn.place(x=10, y=10)






# boucle principale
app.mainloop()
