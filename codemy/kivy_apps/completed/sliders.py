import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.uix.slider import Slider 

#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("sliders.kv")

class MyLayout(Widget):
    def slide_it(self, *args):
        # print(args[1])
        self.slider_text.text = str(int(args[1]))
        self.slider_text.font_size= str(int(args[1]*10))

        

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

