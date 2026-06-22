import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
# from kivy.uix.image import Image
from kivy.core.window  import Window

#set the app size 
Window.size = (300, 500)

#Designate my kv design file
Builder.load_file("calculator.kv")

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    #create a button pressing function 
    def button_press(self, button ): 
        #create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text 

        #test for error first
        if "Error" in prior : 
            prior = ""
        #determine if o is sitting there 
        if prior == "0": 
            self.ids.calc_input.text =''
            self.ids.calc_input.text = f"{button}"
        else: 
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{prior}{button}'

    #create function 
    def remove(self, ):
        prior =self.ids.calc_input.text 
        prior = prior[:-1]
        self.ids.calc_input.text =prior
        #test to see of there's a - sign 
        if  "-" in  prior : 
            self.ids.calc_input.text = f"{prior.replace("-", "")}"
        else:
            self.ids.calc_input.text = f"-{prior}"

    def pos_neg(self):
        prior = self.ids.calc_input.text 
                #test to see of there's a - sign 
        if  "-" in  prior : 
            self.ids.calc_input.text = f"{prior.replace("-", "")}"
        else:
            self.ids.calc_input.text = f"-{prior}"

    #create decimal function 
    def dot(self):
        prior = self.ids.calc_input.text
        #split out text box by + 
        num_list = prior.split("+")
    
        if "+" in prior and "." not in num_list[-1] : 
            prior =f"{prior}."
            #add a decimal to the end of text 
            self.ids.calc_input.text = prior 

        elif "." in prior : 
            pass 
        else: 
            prior =f"{prior}."
            #add a decimal to the end of text 
            self.ids.calc_input.text = prior 

    #add function 
    def math_sign(self, sign ): 
        prior = self.ids.calc_input.text 
        # slap a plius sign to the text box
        self.ids.calc_input.text = f"{prior}{sign}"  

    #equals function 
    def equals_function(self, ):
        prior = self.ids.calc_input.text 
        #Error Handling 
        try :      
            #evualate the math from the text 
            answer = eval(prior)
            #output the answer 
            self.ids.calc_input.text = str(answer) 
        except: 
            self.ids.calc_input.text = "Error"


        # #addition 
        # if "+" in prior : 
        #     num_list = prior.split("+")
        #     answer = 0.0 
        #     #loop thru our list 
        #     for number in num_list : 
        #         answer = answer + float(number)
        #     #print the answer in the text box 
        #     self.ids.calc_input.text = str(answer) 
        
        # elif "-" in prior : 
        #     pass 
        # elif "x" in prior : 
        #     pass
        # elif "/" in prior : 
        #     pass


class CalculatorApp(App):
    def build(self ):
        # Window.clearcolor= (1,1,1,1)
        return MyLayout()
    


if __name__ == '__main__':
    CalculatorApp().run()
    
