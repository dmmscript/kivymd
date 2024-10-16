from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window 

class ManipulaJanela:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def ajustar_tamanho_janela(self):
        Window.size = (self.largura, self.altura)

class MeuApp(MDApp):
    def build(self):
        manipulador = ManipulaJanela(400, 600)
        manipulador.ajustar_tamanho_janela()
        
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20 )
        self.numero1 = MDTextField(hint_text="Digite o primeiro número", input_filter="float") 
        
        self.numero2 = MDTextField(hint_text="Digite o segundo número",input_filter="float") 
        
        botao_somar = MDRaisedButton(text="Somar", on_release=self.somar_numeros)

        self.resultado = MDLabel(text="Resultado: ", halign="center" )

        layout.add_widget(self.numero1)
        layout.add_widget(self.numero2)
        layout.add_widget(botao_somar)
        layout.add_widget(self.resultado)
        return layout

    def somar_numeros(self, instance):
        try:
            num1 = float(self.numero1.text)
            num2 = float(self.numero2.text)
            soma = num1 + num2
            self.resultado.text = f"Resultado: {soma}"
        except ValueError:
            self.resultado.text = "Por favor, insira números válidos"

MeuApp().run()