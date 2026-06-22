from tkinter import * 


class App(Tk):
    "Class for creating an app "
    def __init__(self):
        super().__init__()
        self.title(" OOP Calculator")
        self.iconbitmap("lorem.ico")
        self.geometry("500x800")

        #create widgets 
        self.my_entry =Entry(self, width=25 , font=("Helvetica", 24))
        self.my_entry.pack(pady=20)


        #create a new frame to hold the button 
        My_frame = Frame(self)

class My_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        #create buttons 
        button_1 = Button(self, text="1", font=("Helvetica", 24))
        button_2 = Button(self, text="2", font=("Helvetica", 24))
        button_3 = Button(self, text="3", font=("Helvetica", 24))

        button_4 = Button(self, text="4", font=("Helvetica", 24))
        button_5 = Button(self, text="5", font=("Helvetica", 24))
        button_6 = Button(self, text="6", font=("Helvetica", 24))

        button_7 = Button(self, text="7", font=("Helvetica", 24))
        button_8 = Button(self, text="8", font=("Helvetica", 24))
        button_9 = Button(self, text="9", font=("Helvetica", 24))

        button_0 = Button(self, text="0", font=("Helvetica", 24))
        button_negative=Button(self, text="-/+", font=("Helvetica", 24))
        button_equal = Button(self, text="=", font=("Helvetica", 24))

        button_plus = Button(self, text="+", font=("Helvetica", 24))
        button_minus = Button(self, text="-", font=("Helvetica", 24))
        button_multiply = Button(self, text="*", font=("Helvetica", 24))

        button_divide = Button(self, text="/", font=("Helvetica", 24))
        button_clear = Button(self, text="Clear", font=("Helvetica", 24))

        #grid the buttons to the screen 
        # self.button_1.grid(row= , column= ipadx= , ipady =)

#define and instantiate our app 
app = App()
app.mainloop()

