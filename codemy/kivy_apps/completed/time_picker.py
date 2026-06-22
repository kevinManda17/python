import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker


#set the app size 
Window.size = (700, 500)

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file("time_picker.kv")

    #get the time
    def get_time(self, instance , time):
        self.root.ids.time_label.text= str(time)



    #click cnacel
    def on_cancel(self, instance, time  ):
        self.root.ids.time_label.text= "You Clicked Cancel"

    def show_time_picker(self):
        from datetime import datetime
        

        #define default time
        default_time = datetime.strptime("4:20:00", "%H:%M:%S")
        time_dialog = MDTimePicker()
        #set default time 
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time = self.get_time)
        time_dialog.open()

MainApp().run()

