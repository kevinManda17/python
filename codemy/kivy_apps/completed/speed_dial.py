import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp


#set the app size 
Window.size = (500, 500)

class MainApp(MDApp):

    data = {
        "Python":"language-python", 
        "Ruby":"language-ruby",
        "JS":"language-javascript"
    }

    def callback(self, instance): 
        lang = ""
        if instance.icon == "language-python":
            lang ="python"
        elif instance.icon == "language-ruby":
            lang ="ruby"
        elif instance.icon == "language-javascript":
            lang= "javascript"

        self.root.ids.my_label.text = F"You Pressed {lang}"


    def open(self,):
        self.root.ids.my_label.text = f"Open !"

    def close(self,):
        self.root.ids.my_label.text = f"Close !"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file("speed_dial.kv")



MainApp().run()

