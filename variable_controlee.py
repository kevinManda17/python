import tkinter 


def update_label(*args):
    var_label.set(var_entry.get())
    
app=tkinter.Tk()
app.geometry("400x300")
app.title("variables tkinter")
 


var_entry=tkinter.StringVar()
var_entry.trace_add("w",update_label)
entry=tkinter.Entry(app, textvariable=var_entry)



var_label=tkinter.StringVar()
label=tkinter.Label(app,text="", textvariable=var_label)
var_label.set("")
print("label:",var_label.get())




entry.pack()
label.pack()
app.mainloop()