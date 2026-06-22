import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton

#set the app size 
Window.size = (500, 500)

class MainApp(MDApp):
    dialog =None 
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog=MDDialog(
                title=  "Pretty Neat, Right?!",
                text= "This is just some text that goes Here",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release =self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text= "Yes it's Neat",
                        text_color= self.theme_cls.primary_color , on_release= self.neat_dialog
                    ), 
                ],

            )
        self.dialog.open()
    
    def close_dialog(self, obj): 
        self.dialog.dismiss()

    def neat_dialog(self, obj ):
        self.dialog.dismiss()
        #change 
        self.root.ids.my_label.text= "Yes It's Neat"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file("alert_dialog.kv")


MainApp().run()

