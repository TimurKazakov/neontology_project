from kivy.clock import Clock
from kivy.uix.label import Label
import datetime

class Timer(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = '0:00:00'
        self.number = 0
        self.event = None

    def start_timer(self):
        self.event = Clock.schedule_interval(lambda dt: self.update_text(), 1)

    def update_text(self):
        self.number += 1
        self.text = str(datetime.timedelta(seconds=self.number))

    def stop_timer(self):
        self.event.cancel()

    def reset_timer(self):
        self.text = '0:00:00'
        self.number = 0
        self.event = None
