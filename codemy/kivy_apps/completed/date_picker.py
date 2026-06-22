import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker


#set the app size 
Window.size = (700, 500)

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file("date_picker.kv")

    #click ok 
    def on_save(self, instance , value , date_range):
        # print(instance , value , date_range)
        # self.root.ids.date_label.text= f"{str(value)}"
        self.root.ids.date_label.text= f"{str(date_range[0])} - {str(date_range[-1])}"


    #click cnacel
    def on_cancel(self, instance, value ):
        self.root.ids.date_label.text= "You Clicked Cancel"




    def show_date_picker(self):
        # date_dialog= MDModalDatePicker()
        # date_dialog = MDDatePicker(year=2000, month=2, day=14)
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

MainApp().run()

