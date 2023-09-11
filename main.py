from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        # Cria o layout
        layout = BoxLayout(orientation="vertical")

        # Adiciona o widget à GUI
        self.root.add_widget(layout)

        # Adiciona o widget `Label` ao layout
        label = Label(text="Hello, world!")
        layout.add_widget(label)

MyApp().run()