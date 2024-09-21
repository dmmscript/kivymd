from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class MeuApp(MDApp):
    def build(self): 
        objetoBotao = MDRaisedButton(text='Meu primeiro botão') 
        objetoLabel = MDLabel(text='Meu primeiro label') 
        return objetoLabel
 
MeuApp().run()
