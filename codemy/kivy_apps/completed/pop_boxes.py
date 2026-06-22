import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 

#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("pop_boxes.kv")

class MyLayout(Widget):
    def dismiss(self):
        pass

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

