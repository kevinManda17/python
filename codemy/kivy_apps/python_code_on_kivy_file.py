from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

#set the size 
window = (500, 500 )


class MainApp(MDApp):
    some_text ="Hello World"
    our_list = ["ironman", "kevin", "Manda"]
    def build(self): 
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette ="BlueGray"
        return Builder.load_file("python_code_on_kivy_file.kv")
    



MainApp().run()