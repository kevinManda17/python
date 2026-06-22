import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.uix.tabbedpanel import TabbedPanel


#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("tabs.kv")

class MyLayout(TabbedPanel):
    pass 


class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

