import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 

#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("image_viewer.kv")

class MyLayout(Widget):
    def selected(self, filename ):
        try: 
            self.ids.my_image.source = filename[0]
            print(filename[0])
        except: 
            pass

class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

