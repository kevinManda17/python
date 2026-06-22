from kivy.config import Config
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 700)
Config.set('graphics', 'top', 50)


from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp



#set the app size 
Window.size = (500, 500)

class MainApp(MDApp):

    def build(self):
        Window.borderless= True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("remove_title_bar.kv")

    def stop(self):
        pass


MainApp().run()

