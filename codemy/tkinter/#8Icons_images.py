from tkinter import *
from PIL import ImageTk , Image 


root = Tk()
root.geometry("700x700")
root.title("Using Icons and images in Tkinter")
root.iconbitmap("C:/Users/KEVIN/Documents/programming/HOLIDAYS_CURRENT_PROGRAMMING_LEARNING/PYTHON/codemy/tkinter/img/lorem.ico")




image = ImageTk.PhotoImage(Image.open("img/IMG-20240220-WA0039 - Copy.jpg"))
label =  Label(image = image )

label.pack()



button_quit = Button(root , text="Exit Program " , command = root.quit )

button_quit.pack()

root.mainloop()