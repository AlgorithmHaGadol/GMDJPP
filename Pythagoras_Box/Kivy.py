from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout as GL
from kivy.uix.textinput import TextInput
import PB
#commit this chanegss
class LoginScreen(GL):
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = "User name"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text = "Password"))
        self.password = TextInput(password=True,multiline = False)
        self.add_widget(self.password)
    
class GoodGraciousApp(App):
    def build(self):
        return LoginScreen()
if __name__ == "__main__":
    GoodGraciousApp().run()

