from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import  Window

#Set the app size
Window.size = (400,600)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def exit1():
        exit()

    def clear(self):
        self.ids.calc_input.text = '0'

    #Create a button pressing function
    def button_press(self,button):
        # create a variable that contains whatever is in the text box already
        prior = self.ids.calc_input.text

        # Test for error first
        if "Error" in prior:
            prior = ''

        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    #create a funtion to remove last character in text box
    def remove(self):
        prior = self.ids.calc_input.text
        #remove the last item in the text box
        prior = prior[:-1]
        #output back to the text box
        self.ids.calc_input.text = prior

    #create function to make test box positive or negetive
    def pos_neg(self):
        prior = self.ids.calc_input.text
        #text tp see if there's a - sign already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    #Create deimal function
    def dot1(self):
        prior = self.ids.calc_input.text
        # Split out text box by +
        num_list = prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            #add a decimal to the end of the text
            prior = f'{prior}.'
            #output back to the text box
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            #add a decimal to the end of the text
            prior = f'{prior}.'
            #output back to the text box
            self.ids.calc_input.text = prior

    #create addition function
    def operation(self, sign):
        # create a variable that contains whatever is in the text box already
        prior = self.ids.calc_input.text
        # slap a plus sign to the text
        self.ids.calc_input.text = f'{prior}{sign}'

    #creat equals to function
    def equals(self):
        prior = self.ids.calc_input.text
        # Error Handling
        try:
            #evaluate maths from the text box
            answer = eval(prior)
            #output back to the text box
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
        

class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()