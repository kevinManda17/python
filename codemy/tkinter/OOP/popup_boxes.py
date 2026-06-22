from tkinter import * 
from tkinter import messagebox

class App(Tk): 
    def __init__(self ): 
        super().__init__()

        self.title("Tkinter- OOP Popup Boxes ")
        self.iconbitmap("lorem.ico")
        self.geometry("700x450")
        self.my_label = Label(self, text="Enter your name: ", font=("helvetica", 24))
        self.my_label.pack(pady=20)

        self.my_entry = Entry(self, width=30, font=("helvitica", 24))
        self.my_entry.pack(pady=20)

        self.my_button= Button(self, text="Popup", command=self.popup)
        self.my_button.pack(pady=20)

    def popup(self):
        if self.my_entry.get():
            messagebox.showinfo("Hello", f"Hello {self.my_entry.get()}")
        else: 
            messagebox.showinfo("Error", f"You forgot to type your name ")






app = App()
app.mainloop()
