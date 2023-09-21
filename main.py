from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

GUI = Builder.load_file("tela.kv")


class Webscr(App):
    def build(self):
        # Carregar o arquivo .kv
        return GUI
    def on_start(self):
        # Obter o botão do arquivo .kv
        button = self.root.ids.button

        # Atribuir a função ao botão usando a propriedade 'on_press'
        button.bind(on_press=self.nbgomes)

    def nbgomes(self, instance):
        # Obter o texto do InputText
        text_input = self.root.ids.teste1
        texto = text_input.text
        # Atualizar o texto do rótulo dfjogos
        dfjogos_label = self.root.ids.dfjogos
        dfjogos_label.text = texto

Webscr().run()
