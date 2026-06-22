import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen

#define our different screens 
class FirstWindow(Screen ):
    pass

class SecondWindow(Screen): 
    pass 

class WindowManager(ScreenManager):
    pass 


#set the app size 
Window.size = (500, 500)

#Designate my kv design file
kv = Builder.load_file("multiscreen.kv")

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return kv
    

if __name__ == '__main__':
    AwesomeApp().run()

