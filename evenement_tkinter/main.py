#coding:utf-8
import tkinter 

"""
KeyPress-[touche] : evenement pour le clavier 
Button-1: clique gauche 
Button-2: clique droit 
Button-3: clique du milieu et de la molette 
KP_[chiffre] :  pave numerique 
    KP_Enter:

Escape: 
Space :
Control:
Shift :
Alt:
Double-a 
Control-Alt-a
Double-Button-1

----------------------customize event ------------------
event_add('<<[custome_event]>>' , '[**event]')

"""
def func(event):
    print("Un click s'est produit")

app  = tkinter.Tk()
app.geometry('320x240')


label = tkinter.Label(app, text = 'Hello World ')
app.event_add('<<click>>', '<Button-1>' , '<Button-2>', '<Button-3>' )

app.bind('<<click>>', func)

label.pack()
app.mainloop()