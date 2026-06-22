import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.animation import Animation

#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("animation.kv")

class MyLayout(Widget):
    def animate_it(self, widget, *args): 
        #Define animation you want to do
        animate = Animation(
            background_color= (0,0,1,1),
            duration= 3, 
        )
        #Do second animation 
        animate += Animation(duration= .5, 
        size_hint = (1,1),
        )

        #Do Third animation 
        animate += Animation(duration= .5, 
        size_hint = (.5,.5),
        )
        animate += Animation(
                pos_hint ={"center_x":1} ) 
        animate += Animation(
            pos_hint ={"center_x":0.5} ) 
        
        #start the animation 
        animate.start(widget)

        animate.bind(on_complete = self.my_callback)

    def my_callback(self, *args ):
            self.ids.my_label.text = "Wow Look At That"

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

