from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from screens.MainScreen import MainScreen



class NeonatologyApp(App):
    def build(self):
        return sm



if __name__ == '__main__':
    app = NeonatologyApp()

    sm = ScreenManager()
    main_screen = MainScreen(name='main_screen')
    sm.add_widget(main_screen)
    app.sm = sm
    app.run()