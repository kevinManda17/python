import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
# from kivy.uix.image import Image

#Designate my kv design file
Builder.load_file("update_label.kv")

class MyLayout(Widget):
    def press(self):
        #create varaibles for widgets 
        name = self.ids.name_input.text
        print(name)

        #update the label
        self.ids.name_label.text = name  
        # clear input box 
        self.ids.name_input.text=""
        
class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    


if __name__ == '__main__':
    AwesomeApp().run()
    
