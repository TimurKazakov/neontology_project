from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<Reflexes>:
    rows : 2
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1
        Line:
            width: 2
            rectangle: self.x, self.y, self.width, self.height
    Label:
        text: 'Рефлексы'    
    GridLayout:
        cols: 3
        Button:
            text: 'Отсутвуют'
            on_press: root.bg(self,'0'); 
        
        Button:
            text: 'Гримаса'
            on_press: root.bg(self,'1'); 
        
        Button:
            text: 'Кашель' 
            on_press: root.bg(self,'2'); 



''')


class Reflexes(GridLayout):
    apgar = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.apgar = '0'

    def bg(self, btn, apgar):
        self.apgar = apgar
        btn.background_color = (1, 1, 0, .5)
        App.get_running_app().sm.get_screen('main_screen').calc_apgar()
