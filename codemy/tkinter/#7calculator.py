from tkinter import * 

root = Tk()

# root.geometry("600x300")
root.title("Calculator")

# fg = "white"  , bg ="black"
e = Entry(root ,  width= 75 ,borderwidth=3 , )    

e.grid(row=0, column=0 , columnspan= 3 , padx=3 , pady=10  )


# e.pack()
# e.insert(0 , "Enter Your Name ")


# let define some functions just here 
def buttonclick(num):
    # e.delete(0, END )
    current = e.get()
    e.delete(0, END )
    e.insert(0 , str(current) + str(num) )
    
def buttonClear():
    e.delete(0 , END )

def buttonEqual():
    second_number= e.get()
    e.delete(0 , END )

    if math == "addition":
         e.insert(0 , f_num + float(second_number))
    elif math == "subtraction":
         e.insert(0 , f_num - float(second_number))
    elif math == "division":
         e.insert(0 , f_num / float(second_number))
    elif math == "multiplication":
         e.insert(0 , f_num * float(second_number))
    else : 
         e.insert(0 , "ERROR OPERATION" )

def buttonAdd():
    frist_number = e.get()
    global f_num 
    global math 
    math = "addition"
    f_num = float(frist_number)
    e.delete(0 , END )
    
    
def buttonSubtract():
    frist_number = e.get()
    global f_num 
    global math 
    math = "subtraction"
    f_num = float(frist_number)
    e.delete(0 , END )
    
def buttonMultiply():
    frist_number = e.get()
    global f_num
    global math 
    math = "multiplication" 
    f_num = float(frist_number)
    e.delete(0 , END )
    
def buttonDivide():
    frist_number = e.get()
    global f_num
    global math 
    math = "division" 
    f_num = float(frist_number)
    e.delete(0 , END )
    
    
# define buttons here 

button_1 = Button(root , text= "1" , padx= 70 , pady = 20 , command= lambda : buttonclick(1)) 
button_2 = Button(root , text= "2" , padx= 70 , pady = 20 , command= lambda : buttonclick(2)) 
button_3 = Button(root , text= "3" , padx= 70 , pady = 20 , command= lambda : buttonclick(3)) 
button_4 = Button(root , text= "4" , padx= 70 , pady = 20 , command= lambda : buttonclick(4)) 
button_5 = Button(root , text= "5" , padx= 70 , pady = 20 , command= lambda : buttonclick(5)) 
button_6 = Button(root , text= "6" , padx= 70 , pady = 20 , command= lambda : buttonclick(6)) 
button_7 = Button(root , text= "7" , padx= 70 , pady = 20 , command= lambda : buttonclick(7)) 
button_8 = Button(root , text= "8" , padx= 70 , pady = 20 , command= lambda : buttonclick(8)) 
button_9 = Button(root , text= "9" , padx= 70 , pady = 20 , command= lambda : buttonclick(9)) 
button_0 = Button(root , text= "0" , padx= 70 , pady = 20 , command= lambda : buttonclick(0)) 


button_equal = Button(root , text= "=" , padx= 140 , pady = 20 , command= buttonEqual) 
button_clear = Button(root , text= "Clear" , padx= 130 , pady = 20 , command = buttonClear) 

button_add = Button(root , text= "+" , padx= 68 , pady = 20 , command= buttonAdd  ) 
button_subtract = Button(root , text= "-" , padx= 72 , pady = 20 , command= buttonSubtract  ) 
button_multiply = Button(root , text= "x" , padx= 72 , pady = 20 , command= buttonMultiply   ) 
button_divide  = Button(root , text= "/" , padx= 68 , pady = 20 , command= buttonDivide  ) 


# put button on the screen 

button_1.grid(row= 3, column = 2  ,   columnspan= 1)
button_2.grid(row= 3, column = 1  ,   columnspan= 1)
button_3.grid(row= 3, column = 0  ,   columnspan= 1)

button_4.grid(row= 2, column = 2  ,   columnspan= 1)
button_5.grid(row= 2, column = 1  ,   columnspan= 1)
button_6.grid(row= 2, column = 0  ,   columnspan= 1)


button_7.grid(row= 1,  column= 2  ,  columnspan= 1)
button_8.grid(row= 1,  column= 1  ,  columnspan= 1)
button_9.grid(row= 1,  column= 0  ,  columnspan= 1)


button_clear.grid(row= 4 , column = 1, columnspan= 2)
button_0.grid(row= 4, column = 0  ,  columnspan= 1)


button_add.grid(row=5 , column = 0 , columnspan= 1)
button_equal.grid(row= 5 , column = 1, columnspan= 3)



button_divide.grid(row= 6 , column= 0 )
button_subtract.grid(row = 6 , column= 1 )
button_multiply.grid(row= 6 , column= 2 )




# button_0.pack()
# button_1.pack()
# button_2.pack()
# button_3.pack()
# button_4.pack()
# button_5.pack()
# button_6.pack()
# button_7.pack()
# button_8.pack()
# button_9.pack()
# button_add.pack()
# button_clear.pack()
# button_equal.pack()

root.mainloop() 
