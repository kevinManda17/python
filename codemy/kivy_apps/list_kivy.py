from kivy.lang import Builder 
from kivymd.app import MDApp
from kivy.core.window import Window

#set the size of window
Window =(400, 400)

class MainApp(MDApp): 
    title="Simple List"
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.primary_palette= "BlueGray"

        return Builder.load_file("list_kivy.kv")
    
    def presser(self, pressed, list_id): 
        pressed.tertiary_text = f"You pressed {list_id}" 
        pressed.secondary_text = f"You pressed {list_id}" 
        pressed.text = f"You pressed {list_id}" 


MainApp().run()