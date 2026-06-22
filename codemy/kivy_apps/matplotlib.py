from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp


#set the app size 
Window.size = (500, 500)

class MainApp(MDApp):

    def build(self):
        # Window.borderless= True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("matplotlib.kv")

    def stop(self):
        pass


MainApp().run()

