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
"""


def func(event):
    print('Ok')

def close(event):
    print(f"{event.keysym} et  {event.keycode}")
    event.widget.destroy()

    print("La fenetre a ete fermee")

def classFunc(event):
    print('Ok for class')

def openwindow():
    top = tkinter.Toplevel()
    label_w= tkinter.Label(top, text= 'Bonjour')
    top.bind('<Escape>', close)
    label_w.pack()


app  = tkinter.Tk()
app.geometry('320x240')

# entry_w = tkinter.Entry(app)
# entry_w.bind('<Double-Button-1>', func)

# app.bind_class('Entry','Double-Button-2' ,classFunc)

button_w= tkinter.Button(app , text='Ouvrir une fenetre' , command= openwindow)


button_w.pack()
app.mainloop()