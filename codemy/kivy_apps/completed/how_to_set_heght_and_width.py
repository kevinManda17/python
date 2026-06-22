import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 


class MyGridLayout(GridLayout):
    # initialize infinite keywords 
    def __init__(self , **kwargs ):
        # call grid layout constuctor 
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns 
        self.cols= 1 
        self.row_force_default=True
        self.row_default_height=120
        self.col_force_default=True 
        self.col_default_width=100
        #create the second gridlayout 
        self.top_grid = GridLayout()
        # set number of columns in the grid 
        self.top_grid.cols =2 

        # add  widgets 
        self.top_grid.add_widget(Label(text="Name:  ", ))
        # add input box 
        self.name= TextInput(multiline= False, size_hint_y=None, 
        height= 50,
        size_hint_x=None, 
        width=200, )
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorites pizza :  "))
        # add input box 
        self.pizza= TextInput(multiline= False )
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favorites color :  "))
        # add input box 
        self.color= TextInput(multiline= False )
        self.top_grid.add_widget(self.color )

        #add the new top_grid to our app 
        self.add_widget(self.top_grid)

        #create a subtmit button 
        self.submit =Button(text="Submit ", font_size=32,  size_hint_y=None, 
        height= 50,
        size_hint_x=None, 
        width=200, )
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance ):
        name = self.name.text 
        pizza= self.pizza.text 
        color= self.color.text  

        # print(f"Hello {name }, you like {pizza} pizza and your favorite is {color } !")
        self.add_widget(Label(text=f"Hello {name }, you like {pizza} pizza and your favorite is {color } !"))
        #clear the input boxes 
        self.name.text=""
        self.pizza.text=""
        self.color.text=""
 
        
class MyApp(App):
    def build(self ):
        return MyGridLayout()
    


if __name__ == '__main__':
    MyApp().run()
    