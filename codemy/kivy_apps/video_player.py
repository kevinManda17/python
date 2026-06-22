from kivy.lang import Builder 
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer

#pip install ffpyplayer



Window =(400, 400)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.primary_palette="BlueGray"
        # return Builder.load_file("video_player.kv")

        player = VideoPlayer(source="img/ironman.mp4")
        #assign VideoPlayer state
        player.state = 'play'

        player.options ={'eos':'loop'}

        player.allow_stretch =True
        return player


MainApp().run()
