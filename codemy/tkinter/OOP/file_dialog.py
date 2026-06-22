from tkinter import * 
from tkinter import filedialog


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter - File dialog")
        self.iconbitmap('lorem.ico')
        self.geometry("700x450")

        #create Widgets 
        self.my_text = Text(self, width=80, height=20 )  
        self.my_text.pack(pady=20)

        self.my_button = Button(self,text=  "Open File", command=self.file)
        self.my_button.pack(pady=20)
    #create Popup Function 

    def file(self):
        self.my_file = filedialog.askopenfilename(initialdir="", title="Select a File ", filetypes=(("txt files","*.txt", ), ("all files", "*.*")))
    #check to make  sure user selected a file
        if self.my_file: 
            #open and read the file 
            get_contents =open(self.my_file, "r")
            self.my_text.insert(END, get_contents.read())
            
# Define and instantiate our app 
app = App()
app.mainloop()