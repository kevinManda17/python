import tkinter 


def func(event):
    print("La touche [A] a ete pressee ")

app = tkinter.Tk()
app.geometry("320x340")

entry_w= tkinter.Entry(app)
entry_w.bind('<KeyPress-a>', func)


entry_w.pack()
app.mainloop()