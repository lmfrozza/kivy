from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MyApp(App):
    def build(self):
        return GUI
MyApp().run()
a = 1
