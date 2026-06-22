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

        # add  widgets 
        self.add_widget(Label(text="Name:  "))
        # add input box 
        self.name= TextInput(multiline= False )
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorites pizza :  "))
        # add input box 
        self.pizza= TextInput(multiline= False )
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorites color :  "))
        # add input box 
        self.color= TextInput(multiline= False )
        self.add_widget(self.color )

        #create a subtmit button 
        self.submit =Button(text="Submit ", font_size=32)
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
