import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.core.spelling import Spelling
#set the app size 
Window.size = (500, 500)

#Designate my kv design file
Builder.load_file("spell_checker.kv")

class MyLayout(Widget):
    def press(self): 
        #create instance pf spelling
        s = Spelling()

        #selecte the language 
        s.select_language('en_US')

        #see the language options 

        #grab the word fomr the textbox 
        word = self.ids.word_input.text 

        options  = s.suggest(word)
        x = ''
        for item in options:
            x = f'{x}\n{item}'
        # update our label 
        self.ids.word_label.text = f"{x}"
class AwesomeApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()

