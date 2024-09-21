from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

class MeuApp(MDApp):
    def build(self): 
        objetoBotao = MDRaisedButton()
        objetoBotao.text = 'Meu primeiro botão'
        objetoBotao.color = 'yellow'
        objetoBotao.font_size = 20
        #objetoBotao.disabled = True
        return objetoBotao

MeuApp().run()
