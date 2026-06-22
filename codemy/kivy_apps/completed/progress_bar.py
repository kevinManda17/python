import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 


#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("progress_bar.kv")

class MyLayout(Widget):
    def press_it (self):
        #grab the current progress bar value 
        current_value = self.ids.my_progress_bar.value
        if current_value == 1: 
            current_value = 0

        current_value += .25
        self.ids.my_progress_bar.value = current_value
        #update the label 
        self.ids.my_label.text = f"{int(current_value* 100)}% Progress "

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

