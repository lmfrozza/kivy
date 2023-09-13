from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    def on_button_press(self):
        print("Button pressed!")

MeuAplicativo().run()