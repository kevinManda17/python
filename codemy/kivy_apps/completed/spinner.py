import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 

#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("spinner.kv")

class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f"Selected {value}"

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

