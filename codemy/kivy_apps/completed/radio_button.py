import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 

#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("radio_button.kv")

class MyLayout(Widget):
    checks = []
    def checkbox_click(self, instance , value, topping ):
        tops = ''
        if value == True : 
            MyLayout.checks.append(topping)
            for x in MyLayout.checks :
                tops = f"{tops} {x}"
            self.ids.output_label.text = f"You selected : {tops}"
        else: 
            MyLayout.checks.remove(topping)
            self.ids.output_label.text = f"You selected : {tops}"

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

