from kivy.lang import Builder 
from kivymd.app import MDApp
from kivy.core.window import Window 
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label 



#set the window 
window = (200, 200)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.primary_palette ="BlueGray"
        #define our BoxLayout:
        layout = GridLayout(cols=1)
        #define our VkeyBoard
        keyboard= VKeyboard(on_key_up= self.key_up)

        # return Builder.load_file("keyboard.kv")
        self.label = Label(text="Type Something!", font_size= 20)
        layout.add_widget(self.label)
        layout.add_widget(keyboard)
        return layout

    def key_up(self, keyboard, keycode, *args):
        if isinstance(keycode, tuple):
            print(keycode)
            keycode =keycode[1]

        #tracking what was already in the label 
        thing= self.label.text
        
        #Run some logic 
        if thing == "Type Something!":
            thing= ""

        if keycode == "backspace":
            thing= thing[:-1]
            keycode= ""

        if keycode == "spacebar":
            keycode = " "

        #update the label 
        self.label.text= F"{thing}{keycode}"

        


MainApp().run()
