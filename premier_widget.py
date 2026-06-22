import tkinter 

app=tkinter.Tk()

# label_welcome=tkinter.Label(app, text="bienvenu a tous ")
# label_welcome.configure(text="le nouveau message ")
# label_welcome.pack()
# app.mainloop()
# message_welcome=tkinter.Message(app, text="bienvenu a tous ")
# message_welcome.configure(text="le nouveau message ")
# message_welcome.pack()
# entry_name=tkinter.Entry(app, show="+")
# entry_name.pack()
def hello():
    print("hello sur le terminal")
button_quit=tkinter.Button(app, text="ok", command=hello)

button_quit.pack()
app.mainloop()