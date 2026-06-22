from tkinter import * 

class App(Tk):
    def __init__(self ):
        super().__init__()

        #title ,icon , size 
        self.title("My App For Objetc Oriented Progamming")
        self.iconbitmap("lorem.ico")
        self.geometry("700x450")

        #create status variable
        self.status = True

        #create some widgets 
        self.my_label = Label(self, text ="Hello World !", font=("Helvetica", 24))
        self.my_label.pack(pady = 20)
        self.my_button = Button(self, text = "Change Text !", command = self.change)
        self.my_button.pack(pady = 20)
        My_frame(self)  
    # create a frame outside of this function 
    
    def change(self):
        if self.status:
            self.my_label.config(text = "GoodBye World ! ")
            self.status = False
        else:
            self.my_label.config(text = "Hello World ! ")
            self.status = True

class My_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #put this sucker on the screen 
        self.pack(pady = 20)

        #create a few buttons 
        self.my_button1 = Button(self, text = "Change")
        self.my_button2 = Button(self, text = "Change")
        self.my_button3 = Button(self, text = "Change")

        self.my_button1.grid(row = 0, column = 0)
        self.my_button2.grid(row = 0, column = 1)
        self.my_button3.grid(row = 0, column = 2)


#define and instantiate our app 
app = App()
app.mainloop()