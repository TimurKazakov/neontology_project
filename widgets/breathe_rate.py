from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<BreatheRate>:   
    rows : 3
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1
        Line:
            width: 2
            rectangle: self.x, self.y, self.width, self.height
    Label:
        text: 'Частота дыхания'
    TextInput:
        text: root.breathe_rate
       
    GridLayout:
        cols: 3
        Button:
            text: '20'
            on_press: root.update_breathe_rate(20,self)
        Button:
            text: '40'
            on_press: root.update_breathe_rate(40,self)
        Button:
            text: '60' 
            on_press: root.update_breathe_rate(60,self)     



''')


class BreatheRate(GridLayout):
    breathe_rate = StringProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.breathe_apgar = '0'

    def update_breathe_rate(self, breath_rate, btn):
        btn.background_color = (1, 1, 0, .5)
        self.breathe_rate = f'{breath_rate}'
        if breath_rate <= 20:
            self.breathe_apgar = 0
        elif 20 <= breath_rate <= 40:
            self.breathe_apgar = 1
        else:
            self.breathe_apgar = 2
        App.get_running_app().sm.get_screen('main_screen').calc_apgar()