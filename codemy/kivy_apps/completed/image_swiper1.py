import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp

#set the app size 
Window.size = (500, 500)

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file("image_swiper1.kv")

    def on_swipe_left(self):
        self.root.ids.toolbar.title ="You Swiped Left"


    def on_swipe_right(self): 
        self.root.ids.toolbar.title ="You Swiped Right"


MainApp().run()

