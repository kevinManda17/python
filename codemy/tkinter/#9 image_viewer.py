from tkinter import *
from PIL import ImageTk , Image 


root = Tk()
# root.geometry("1080x1080")
root.title("Using Icons and images in Tkinter")
root.iconbitmap("img/lorem.ico")


# set path for images 
image = ImageTk.PhotoImage(Image.open("img/k.jpg"))
image1 = ImageTk.PhotoImage(Image.open("img/IMG-20240329-WA0065.jpg"))
image2 = ImageTk.PhotoImage(Image.open("img/IMG-20240329-WA0066.jpg"))
image3 = ImageTk.PhotoImage(Image.open("img/IMG-20240329-WA0067.jpg"))
image4 = ImageTk.PhotoImage(Image.open("img/IMG-20240329-WA0068.jpg"))
image5 = ImageTk.PhotoImage(Image.open("img/IMG-20231126-WA0107.jpg"))



image_list = [ image , image1 , image2 , image3 , image4 , image5 ]

status = Label(root , text= "Image 1 of " + str(len(image_list)) , bd = 1, relief = SUNKEN  , anchor= E )

# define some functions 
def forward(image_num):
    global label 
    global button_forward 
    global button_back 

    label.grid_forget()
    label = Label(image = image_list[image_num - 1])
    button_forward = Button(root , text=">> ", command = lambda : forward(image_num +1 )) 
    button_back = Button(root , text =" <<" , command = lambda : back(image_num -1 )) 

    if image_num  == 6 : 
        button_forward = Button(root , text = ">> " , state=DISABLED)

    label.grid(row = 0 , column= 0  , columnspan= 3 )

    button_back.grid(row =   1, column= 0 )
    button_forward.grid(row= 1 , column=2  )

    status = Label(root , text= f"Image {image_num} of  {str(len(image_list)) } "   , bd = 1, relief = SUNKEN  , anchor= E )
    status.grid(row = 2 , column= 0  , columnspan= 3 , sticky= W+E)


def back(image_num):
    global label 
    global button_forward 
    global button_back 

    label.grid_forget()
    label = Label(image = image_list[image_num - 1])
    button_forward = Button(root , text=">> ", command = lambda : forward(image_num +1 )) 
    button_back = Button(root , text =" <<" , command = lambda : back(image_num -1 )) 

    if image_num  == 1 : 
        button_back = Button(root , text = " <<" , state=DISABLED)

    label.grid(row = 0 , column= 0  , columnspan= 3 )

    button_back.grid(row =   1, column= 0 )
    button_forward.grid(row= 1 , column=2  )
    
    status = Label(root , text= f"Image {image_num} of  {str(len(image_list)) } "   , bd = 1, relief = SUNKEN  , anchor= E )
    status.grid(row = 2 , column= 0  , columnspan= 3 , sticky= W+E)



# convert into tkinter stuff 
label =  Label(image = image )


# put tkinker stuff on the screen 
label.grid(row = 0 , column= 0  , columnspan= 3 )


# define some buttons and putting on the screen 
button_back = Button(root , text = " <<" , command = back , state = DISABLED  )
button_quit = Button(root , text="Exit Program " , command = root.quit )
button_forward =Button (root , text = " >> " , command = lambda : forward(2))

button_back.grid(row = 1  , column= 0  )
button_quit.grid(row= 1 , column= 1)
button_forward.grid(row= 1 , column= 2 ,pady = 10  )
status.grid(row = 2 , column= 0  , columnspan= 3 , sticky= W+E)

# loop for app 
root.mainloop() 
