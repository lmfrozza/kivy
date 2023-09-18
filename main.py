from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import requests

GUI = Builder.load_file("tela.kv")


class Webscr(App):
    def build(self):
        return GUI
Webscr().run()
