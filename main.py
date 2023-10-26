from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


GUI = Builder.load_file("tela.kv")
vercod = 10

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
    dfjogos_label = self.root.ids.dfjogos
    global vercod
    global Pesquisa
    global nome_jogo
    global progress_bar
    text_input = self.root.ids.teste1
    Pesquisa = text_input.text
    progress_bar = self.root.ids.progress_bar
    #dfjogos_label.text = "Processando..."
    Steam()
    if vercod >= 15:

      progress_bar.value = 25
      microsoft()
      progress_bar.value = 50
      gog()
      progress_bar.value = 75
      psn()
      progress_bar.value = 100
      dfjogos_label.text = (f'{nome_jogo} Steam: {preco_steam_texto} Xbox: {preco_microsoft_texto} PSN: {preco_PSN} GOG: {preco_GOG}')
    else: 
      progress_bar.value = 25
      sleep(2)
      progress_bar.value = 50
      sleep(2)
      progress_bar.value = 75
      sleep(2)
      progress_bar.value = 100
      sleep(2)
      dfjogos_label.text = "Error 404"


def Steam():
  global nome_jogo
  global vercod
  global preco_steam_texto
  try:
    browser.get('https://store.steampowered.com/')
    # Encontra o elemento do site pelo id htlm
    pesquisa_steam = browser.find_element('id', 'store_nav_search_term')
    sleep(3)
    pesquisa_steam.send_keys(Pesquisa)
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
  except:
    vercod = vercod+10


def microsoft():
  global preco_microsoft_texto
  
  browser.get('https://www.xbox.com/pt-BR')
  botao_microsoft = browser.find_element('id', 'search')
  botao_microsoft.click()
  sleep(3)
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
def gog():
  global preco_GOG

  browser.get('https://www.gog.com/pt/games')
  browser.find_element('xpath', '//*[@id="Catalog"]/div/div[1]/filters-wrapper/div/div[1]/div[2]/div/div/div/filters/div/collapsible-section/div[2]/div/label/input').click()
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
def psn():
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

  

    
    
edge_options = Options()
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')

browser = wd.Edge(options=edge_options)  #options=edge_options



Webscr().run()
browser.quit()