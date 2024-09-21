from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.fitimage import FitImage
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class ManipulaJanela:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def ajustar_tamanho_janela(self):
        Window.size = (self.altura, self.largura)

class MundoDosCiliosApp(MDApp):
    def build(self):
        manipulador = ManipulaJanela(600, 800)
        manipulador.ajustar_tamanho_janela()

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "200"

        layout = FloatLayout()
        
        # Adicionando a imagem de fundo
        background = Image(source='mundodoscilios.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        box_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        servicos = [
            ("Sobre Nós", "aboutus.jpg"),
            ("Russian Volume", "russianvolume.jpg"),
            ("Fox Eyes", "foxeyes.jpg"),
            ("Mega Volume", "megavolume.jpg"),
            ("Classic", "classic.jpg"),
            ("Hybrid", "hybrid.jpg")
        ]
        
        for servico, imagem in servicos:
            grid = MDGridLayout(cols=2, adaptive_height=True)
            img = FitImage(source=imagem, size_hint=(None, None), size=(100, 100))
            botao = MDRaisedButton(text=servico, on_release=self.mostrar_servico)
            grid.add_widget(img)
            grid.add_widget(botao)
            box_layout.add_widget(grid)

        layout.add_widget(box_layout)

        return layout

    def mostrar_servico(self, instance):
        if instance.text == "Sobre nós":
            print("No Mundo dos Cílios, nossa missão é realçar sua beleza natural com carinho e dedicação. Localizados em Videira, SC, somos especializados em extensão de cílios, oferecendo um atendimento personalizado que vai além de um simples serviço: queremos que você se sinta única e especial em cada visita. Nosso compromisso é proporcionar uma experiência acolhedora e relaxante, com muita atenção aos detalhes. Sabemos que você merece o melhor, e estamos aqui para cuidar de você, mimando cada cliente como se fosse a única. Aqui, beleza e bem-estar caminham lado a lado! Venha nos conhecer e descubra o que faz do Mundo dos Cílios o lugar perfeito para transformar seu olhar. Você não vai se arrepender!")
        elif instance.text == "Fox Eyes":
            print("Cílios mais longos no canto externo, criando um efeito alongado e levantado, semelhante ao formato dos olhos de uma raposa.")
        elif instance.text == "Russian Volume":
            print("Aplicação de múltiplos cílios finos em cada cílio natural, resultando em um visual denso, volumoso e dramático.")
        elif instance.text == "Classic":
            print("Uma extensão aplicada em cada cílio natural, proporcionando um visual mais natural e definido.")
        elif instance.text == "Hybrid":
            print("Combinação de técnicas clássica e volume, criando um equilíbrio entre densidade e naturalidade.")
        elif instance.text == "Mega Volume":
            print("Semelhante ao Russian Volume, porém com mais cílios aplicados por fio natural, para um visual ainda mais denso e dramático.")

MundoDosCiliosApp().run()
