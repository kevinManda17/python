import tkinter

mainapp= tkinter.Tk()
mainapp.title("mon premier programme fenetre")
# mainapp.minsize(640,480)
# mainapp.maxsize(1250,780)
# mainapp.geometry("800x600")
screen_x=mainapp.winfo_screenwidth()
screen_y=mainapp.winfo_screenheight()
window_x=800
window_y=600
posX=(screen_x//2)-(window_x//2)
posY=(screen_y//2)-(window_y//2)
geo="{}x{}+{}+{}".format(window_x, window_y,posX,posY)
mainapp.geometry(geo)
# mainapp.resizable(width=False, height=False)
mainapp.mainloop()
