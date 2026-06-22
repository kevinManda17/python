from tkinter import * 

root = Tk()


def myClick():
    myLabel = Label(root , text = "Look i clicked button !")
    myLabel.pack()


myButton = Button(root , text = "Click me " , padx = 50 , pady = 100)

myButton.pack()

root.mainloop()