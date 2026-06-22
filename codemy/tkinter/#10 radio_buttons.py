from tkinter import *
from PIL import ImageTk , Image 


root = Tk()
# root.geometry("1080x1080")
root.title("Radio Buttons with tkinter ... ")
root.iconbitmap("img/lorem.ico")


# r = IntVar()
# r.get()


MODES  = [
        ("Pepperoni" , "Pepperoni") , 
        ("Cheese" , "Cheese") , 
        ("Mushroom" , "Mushroom" ) , 
        ("Onion" ,  "Onion") , 
]

pizza  = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES :
    Radiobutton(root , text = text  , variable= pizza , value = mode ).pack()


def clicked (value ):
    myLabel = Label (root , text = value )
    myLabel.pack()

# Radiobutton(root , text = "Option 1 " , variable= r , value  = 1 , command = lambda : clicked(r.get())).pack()
# Radiobutton(root , text = "Option 2 " , variable= r , value  = 2 , command = lambda : clicked(r.get())).pack()

myLabel  = Label(root , text = pizza.get())
myLabel.pack()

mybutton = Button(root , text = "Click me " , command = lambda : clicked(pizza.get())) 
mybutton.pack()



# loop for app 
root.mainloop() 
