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
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file("login.kv")


    def logger(self):
        self.root.ids.welcome_label.text =f"Sup {self.root.ids.user.text} !"

    def clear(self):
        self.root.ids.welcome_label.text ="WELCOME"
        self.root.ids.user.text =""
        self.root.ids.password.text =""




MainApp().run()

