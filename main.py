from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

GUI = Builder.load_file("tela.kv")


Pesquina = ""  # Movido para um escopo global
nome_jogo = ""

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
    global Pesquina
    global nome_jogo
    text_input = self.root.ids.teste1
    Pesquina = text_input.text
    Buscar()


    # Atualizar o texto do rótulo dfjogos
    dfjogos_label = self.root.ids.dfjogos
    dfjogos_label.text = (f'{nome_jogo} Steam: {preco_steam_texto} Xbox: {preco_microsoft_texto} PSN: {preco_PSN} GOG: {preco_GOG}')


edge_options = Options()
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')

browser = wd.Edge(options=edge_options)  #options=edge_options

def Buscar():
  global preco_microsoft_texto
  global preco_steam_texto
  # Abre o link
  browser.get('https://store.steampowered.com/')
  # Encontra o elemento do site pelo id htlm
  pesquisa_steam = browser.find_element('id', 'store_nav_search_term')
  pesquisa_steam.send_keys(Pesquina)
  sleep(3)
  try:
    # pesquisa_steam.send_keys(Keys.DOWN)
    # pesquisa_steam.send_keys(Keys.ENTER)
    preco_steam = browser.find_element('class name', 'match_subtitle')
    nome_steam = browser.find_element('class name', 'match_name ')
    nome_jogo = nome_steam.text
    preco_steam_texto = preco_steam.text
  except:
    preco_steam_texto = "Ausente"


  browser.get('https://www.microsoft.com/pt-br/store/collections/pcgavtaz')
  botao_microsoft = browser.find_element('id', 'search')
  botao_microsoft.click()
  pesquisa_microsoft = browser.find_element('xpath', '//*[@id="cli_shellHeaderSearchInput"]')

  print(nome_jogo)
  pesquisa_microsoft.send_keys(nome_jogo)
  print(pesquisa_microsoft)
  sleep(3)
  
  (browser.find_element('class name', 'c-menu-item')).click()
  sleep(6)
  try:
      elemento_game_pass = browser.find_element('class name', 'high-contrast')
      preco_microsoft_texto = "29,99/mês (GamePass)"
  except:
    try:
      xpath = "//div[contains(@class, 'ProductDetailsHeader-module__showOnMobileView___uZ1Dz')]//span[contains(@class, 'Price-module__boldText___vmNHu')]"
      div_containing_span = browser.find_element('class name', 'ProductDetailsHeader-module__showOnMobileView___uZ1Dz')
      span = browser.find_element('xpath', xpath)
      preco_microsoft_texto = span.get_attribute('innerText')
    except:
        preco_microsoft_texto = "Ausente"
  global preco_GOG
  browser.get('https://www.gog.com/pt/games')
  xpath= '//*[@id="catalogHeader"]/search/form/input'
  pesquisa_GOG= browser.find_element('xpath', xpath)
  try:
    pesquisa_GOG.send_keys(nome_jogo)
    sleep(3)
  except: 
    pesquisa_GOG.send_keys(Pesquina)
    sleep(3)
  try:
    preco= browser.find_element('xpath', '//*[@id="Catalog"]/div/div[2]/paginated-products-grid/div/product-tile/a/div[2]/div[2]/div/product-price/price-value/span[1]')
    preco_GOG = preco.text
    sleep(3)
  except:
    preco_GOG = "Ausente"
  global preco_PSN
  browser.get('https://store.playstation.com/pt-br/pages/latest')
  (browser.find_element('class name', 'shared-nav-search-container')).click()
  pesquisa_PSN = browser.find_element('class name', 'search-text-box__input')
  try:
    pesquisa_PSN.send_keys(nome_jogo)
    sleep(3)
  except: 
    pesquisa_PSN.send_keys(Pesquina)
    sleep(3)
  (browser.find_element('xpath', '/html/body/div[7]/div/div/div/button[2]')).click()
  try:
    preco = browser.find_element('xpath', '//*[@id="main"]/section/div/ul/li[1]/div/a/div/section/div/div/span')
    preco_PSN = preco.text
  except:
    preco_PSN = "Ausente"


Webscr().run()
browser.quit()