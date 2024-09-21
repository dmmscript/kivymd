from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class MeuApp(MDApp):
    def build(self): 
        objetoBotao = MDRaisedButton(text='Meu primeiro botão') 
        objetoLabel = MDLabel(text = 'Meu primeiro label') 
        objetoBoxLayout = MDBoxLayout()
        objetoBoxLayout.add_widget(objetoLabel)
        objetoBoxLayout.add_widget(objetoBotao)
        return objetoBoxLayout
    
MeuApp().run()