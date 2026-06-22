from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp
from kivy.garden.mapview import MapView
#pip install mapview , garden mapview 

#set the app size 
Window.size = (500, 500)

class MapViewApp(MDApp):

    def build(self):
        mapview_gloabal = MapView()
        mapview =MapView(zoom=10, lat=36, lon= -115)
        return mapview


MapViewApp().run()

