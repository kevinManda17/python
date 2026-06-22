from tkinter import * 

root = Tk()


def myClick():
    myLabel = Label(root , text = "Look i clicked button !")
    myLabel.pack()


myButton = Button(root , text = "Click me " , command = myClick , fg ="red" , bg = "black")

myButton.pack()

root.mainloop() 