import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 


#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("img_button.kv")

class MyLayout(Widget):
    def hello_on(self): 
        self.ids.my_label.text = "You Pressed The Button !"
        self.ids.my_image.source= "img/img_button1.png"

    def hello_off(self): 
        self.ids.my_image.source= "img/img_button.jpg"

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

