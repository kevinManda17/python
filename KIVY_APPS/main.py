import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
import random 

kivy.require('2.3.0')

class GameView(BoxLayout):
    def __init__(self):
        super(GameView, self ).__init__()
        self.randomValue =random.randint(0, 20)

    def check_number(self):
        if int(self.answer_input.text) == self.randomValue :
            self.result_label.text="Congratutions!"
            self.result_label.color="#00EF0B"
            self.randomValue = random.randint(0, 1000)
        elif  int(self.answer_input.text) > self.randomValue :
            self.result_label.text="More !"
            self.result_label.color="#EF3E00"
        elif  int(self.answer_input.text) < self.randomValue :
            self.result_label.text="Less !"
            self.result_label.color="#EF3E00"


class KevinApp(App):
    def build(self):
        return GameView()
    
kevinApp =KevinApp()
kevinApp.run()