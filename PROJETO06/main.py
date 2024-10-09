from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.fitimage import FitImage
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar

class ManipulaJanela:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def ajustar_tamanho_janela(self):
        Window.size = (self.altura, self.largura)
     
class MinhaAgenda(Screen):
    pass

class RedesSociais(Screen):
    pass

class MundoDosCiliosApp(MDApp):
    def build(self):
        manipulador = ManipulaJanela(600, 800)
        manipulador.ajustar_tamanho_janela()

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "200"

        sm = ScreenManager()
        tela_principal = Screen(name='principal')
        layout = MDBoxLayout()

        background = Image(source='mundodoscilios.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        box_layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        servicos = [
            ("Sobre Nós", "sobrenos.png"),
            ("Nossa Equipe", "nossaequipe.png"),
            ("Efeito Fox", "efeitofox.png"),
            ("Efeito Harmony","efeitoharmony.png"),
            ("Técnica Hibrido","tecnicahibrido.png"),
            ("Volume Power","volumepower.png"),
            ("Volume Light","volumelight.png"),
            ("Volume Brasileiro","volumebrasileiro.png"),
            ("Volume Russo","volumerusso.png"),
            ("Volume Clássico","volumeclassico.png"),
            ("SOS Capilar","soscapilar.png"),
            ("Cursos","cursos.png")]

        for servico, imagem in servicos:
            grid = MDGridLayout(cols=2, adaptive_height=True)
            img = FitImage(source=imagem, size_hint=(None, None), size=(50,50))
            botao1 = MDRaisedButton(text=servico, on_release=self.mostrar_servico)
            grid.add_widget(img)
            grid.add_widget(botao1)
            box_layout.add_widget(grid)
            
        layout.add_widget(box_layout)
        tela_principal.add_widget(layout)
        sm.add_widget(tela_principal)

        sm.add_widget(MinhaAgenda(name="Minha Agenda"))
        sm.add_widget(RedesSociais(name="Redes Sociais"))
        sm.add_widget(SobreNos(name="Sobre Nós"))
        sm.add_widget(NossaEquipe(name="Nossa Equipe"))
        sm.add_widget(EfeitoFox(name="Efeito Fox"))
        sm.add_widget(EfeitoHarmony(name="Efeito Harmony"))
        sm.add_widget(TecnicaHibrido(name="Técnica Hibrido"))
        sm.add_widget(VolumePower(name="Volume Power"))
        sm.add_widget(VolumeLight(name="Volume Light"))
        sm.add_widget(VolumeBrasileiro(name="Volume Brasileiro"))
        sm.add_widget(VolumeRusso(name="Volume Russo"))
        sm.add_widget(VolumeClassico(name="Volume Clássico"))
        sm.add_widget(SosCapilar(name="SOS Capilar"))
        sm.add_widget(Cursos(name="Cursos"))

    def mostrar_servico(self, instance):
        self.root.current = instance.text
       
        navigation_layout = MDNavigationLayout(
            ScreenManager(
                MDTopAppBar(
                    pos_hint={"top": 1},
                    elevation=4,
                    title="Mundo dos Cílios",
                    right_action_items=[["menu", lambda x: self.nav_drawer_open()]],
                ),
                   ScreenManager(
                        Screen(
                            MDLabel(
                                text="Minha Agenda",
                                halign="center",
                            ),
                            name="Minha Agenda",
                        ),
                        Screen(
                            MDLabel(
                                text="Redes Sociais",
                                halign="center",
                            ),
                            name="Redes Sociais",
                        ),
                        id="screen_manager",
                    ),
                    MDNavigationDrawer(
                        MDScrollView(
                            MDList(
                                OneLineListItem(
                                    text="Minha Agenda",
                                    on_press=self.switch_screen
                                ),
                                OneLineListItem(
                                    text="Redes Sociais",
                                    on_press=self.switch_screen
                                ),
                            ),
                        ),
                        id="nav_drawer",
                        radius=(0, 16, 16, 0),
                    ),
                    id="navigation_layout",
                )
            )

    def switch_screen(self, instance_list_item: OneLineListItem):
        self.root.ids.navigation_layout.ids.screen_manager.current = {
            "Minha Agenda": "Minha Agenda",
            "Redes Sociais": "Redes Sociais"
        }[instance_list_item.text]
        self.root.children[0].ids.nav_drawer.set_state("close")

    def nav_drawer_open(self):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")

class BotaoVoltar(MDIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "arrow-left"
        self.theme_icon_color = "Custom"
        self.icon_color = "#FF6EC7"
        self.size_hint = [.1, .1]
        self.pos_hint = {"center_x": 0.0, "center_y": 0.9}
        
    def on_press(self):
        app = MDApp.get_running_app()
        app.root.current = "principal"

class SobreNos(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        # background = Image(source='sobrenos.png', allow_stretch=True, keep_ratio=False)
        # layout.add_widget(background)
        label = MDLabel(
            text="Se beleza fosse crime, a galera do Mundo dos Cílios "
                "estaria na prisão! A gente capricha na extensão de "
                "cílios e no trato dos seus cabelos pra você sair daqui "
                "tipo 'uau!'. "
                "‘Quem é essa na fila do pão?' "
                "E se a vontade é de aprender todos esses truques, "
                "se torna um empreendedor na área Beauty, nossos "
                "cursos presenciais são exatamente o que você "
                "precisa. "
                "Você pode se tornar uma LASH DESIGNER ou uma "
                "DESIGNER DE SOBRANCELHAS de sucesso. "
                "Aaahh, e não para por aí… "
                "Entre uma transformação e outra, dá uma pausa "
                "deliciosa no nosso Café Gourmet que é servido "
                "especialmente para cada cliente. "
                "Enquanto isso, você pode relaxar porque cuidar de "
                "si também é sobre curtir bons momentos. "
                "A gente está por aqui pra te atender do jeito que "
                "você merece: com carinho e muita atenção!",
            halign="center",
            # pos_hint={"center_x": 0.5, "center_y:": 0.5},
            # theme_text_color="Custom",
            # text_color=(1, 1, 1, 1)
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class NossaEquipe(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="No Mundo dos Cílios, nossa equipe é o coração do estúdio, com a Jessy, nossa "
                "fundadora e lash master, sendo a força por trás do estúdio, trazendo sua "
                "expertise e paixão para cada detalhe. Ela é também quem nos inspira e nos "
                "motiva. Kally, uma talentosa lash master, é conhecida por sua habilidade e "
                "atenção com as nossas clientes. Dani, nossa secretária e lash, desempenha o "
                "seu serviço maravilhosamente bem e todas as clientes amam. Fernanda cria as "
                "melhores ideias para inovar nos atendimentos e cuidar da experiência das nossas "
                "clientes. Kesya é nossa hair stylist, se os seus cabelos estão sem vida, nossa "
                "especialista S.O.S capilar vai desenvolver o melhor protocolo pra você. Cada "
                "membro da nossa equipe traz um toque especial, e juntas, formamos um time "
                "determinado a oferecer uma experiência única e inesquecível. No Mundo dos Cílios, "
                "nossa missão é realçar sua beleza.",
            halign="center"
        )

        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class EfeitoFox(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="O efeito Fox é a tendência do momento no mundo lash, perfeito "
                "para quem ama um olhar poderoso e cheio de atitude. Inspirada nos "
                "olhos de raposa, essa técnica alonga os cílios de um jeito que dá "
                "aquele up no olhar, deixando os cantos externos mais alongados e "
                "garantindo um visual super estiloso e sexy. No Mundo dos Cílios, nossa "
                "lash artist Kaly manda muito bem nessa técnica, criando um design "
                "exclusivo para cada cliente. Se você quer realçar o olhar e ficar por "
                "dentro das novidades, o efeito Fox é a escolha certa!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class EfeitoHarmony(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="O Efeito Harmony é a nova sensação para quem quer dar um toque especial ao "
                "olhar, focando nos fios inferiores. Essa técnica de extensão de cílios é perfeita "
                "para quem busca um visual natural, mas com um toque extra de charme. O "
                "segredo do Efeito Harmony está em aplicar fios de diferentes tamanhos e "
                "curvaturas nos cílios inferiores, criando um look leve e equilibrado que destaca o "
                "olhar de forma sutil e elegante. No Mundo dos Cílios, nossas profissionais "
                "dominam essa técnica, garantindo um design que valoriza a beleza única de "
                "cada cliente. Se você quer inovar e conquistar um olhar harmônico e "
                "sofisticado, o Efeito Harmony é a escolha certa!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class TecnicaHibrido(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="A técnica Híbrida é perfeita para quem quer "
                "cílios mais naturais, mas sem abrir mão de "
                "um toque de glamour. Ela é o equilíbrio ideal "
                "entre o look super volumoso e o mais "
                "discreto. Com a técnica Híbrida, a gente "
                "mistura fios clássicos com fios de volume, "
                "criando um efeito que deixa os cílios mais "
                "cheios, mas sem pesar demais. O resultado é "
                "um olhar mais expressivo, porém bem "
                "natural, como se você tivesse nascido assim! "
                "No Mundo dos Cílios, nossas lash artists "
                "sabem exatamente como alcançar esse look, "
                "deixando você com cílios lindos e na medida "
                "certa, para arrasar no dia a dia com aquele "
                "charme a mais.",
            halign="center"
        )
        layout.add_widget(label)      
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class VolumePower(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="O Volume Power é pra quem quer causar mesmo! Se você é do time "
                "que ama cílios super cheios e pretinhos, essa técnica foi feita "
                "pra você. São vários fios ultrafinos em cada cílio natural, "
                "pra um efeito que grita VOLUME. "
                "Sabe aquele olhar de capa de revista? É isso que o Volume "
                "Power entrega: cílios mega poderosos, cheios de presença. "
                "Mas claro sempre respeitando o visagismo do olhar. "
                "No Mundo dos Cílios, nossas lash artists arrasam nessa técnica, "
                "deixando seus cílios do jeitinho que você gosta: cheios, pretinhos "
                "e perfeitos.",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class VolumeLight(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="O Volume Light é perfeito para quem quer o melhor dos dois "
                "mundos! Ela oferece um efeito intermediário: não é tão "
                "volumosa quanto o Volume Russo, mas também não é tão "
                "discreta quanto as técnicas mais naturais. É o famoso meio-termo, "
                "ideal para quem quer um olhar mais marcante, mas sem "
                "exagerar. No light, a gente mistura fios tecnológicos, "
                "criando um olhar equilibrado. No Mundo dos Cílios, nossas lash "
                "artists arrasam nessa técnica, garantindo cílios perfeitos para "
                "quem quer se destacar, mas ainda manter aquela vibe mais "
                "suave. É a escolha certa pra quem gosta de um visual glam, "
                "mas na medida certa!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class VolumeBrasileiro(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="O Volume Brasileiro é a técnica queridinha do momento e tá bombando por aqui! O "
                "segredo? Ele se adapta totalmente aos seus cílios naturais. Se você tem muitos fios, "
                "se prepara, porque o efeito vai ser bem volumoso e poderoso. Agora, se você tem "
                "menos fios, sem crise! O resultado fica mais leve e natural, mas ainda assim super "
                "charmoso. Ah, e tem mais: dá pra fazer essa técnica nas cores marrom também, pra um "
                "efeito ainda mais natural e elegante. No Mundo dos Cílios, a gente ama essa "
                "versatilidade do Volume Brasileiro, e nossas clientes também! Afinal, não importa se você "
                "quer arrasar com aquele volume de diva ou prefere um look mais sutil, essa técnica tem o "
                "que você precisa. É a tendência do momento, e a gente tá aqui pra deixar seus cílios do "
                "jeitinho que você sempre sonhou!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class VolumeRusso(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="O Volume Russo é o verdadeiro luxo dos cílios! "
                "Essa técnica é pra quem quer um olhar super "
                "dramático e cheio de glamour, sem economizar no "
                "volume. Aqui, a gente aplica vários fios ultrafinos "
                "em cada cílio natural, criando um efeito de "
                "preenchimento máximo e aquele look de 'acabei de "
                "sair do tapete vermelho'. É o tipo de cílio que não "
                "passa despercebido! No Mundo dos Cílios, nossas "
                "lash artists são mestres em Volume Russo, "
                "garantindo um acabamento perfeito, com fios bem "
                "densos e alinhados. Se você quer um olhar "
                "poderoso, impactante e digno de estrela, o Volume "
                "Russo é a escolha certa. Afinal, quem disse que "
                "cílios não podem ser a cereja do bolo do seu look?",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)
        
class VolumeClassico(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="O Volume Clássico é a escolha perfeita pra quem ama aquele "
                "look mais leve e natural. É a técnica mais suave que temos "
                "aqui no estúdio, ideal pra quem quer dar um realce sutil ao olhar, "
                "sem perder a naturalidade. No Volume Clássico, aplicamos um "
                "fio de extensão em cada cílio natural, criando um efeito de "
                "alongamento e definição, mas de um jeito bem discreto. É como se "
                "você tivesse nascido com cílios mais longos e definidos, sabe? No "
                "Mundo dos Cílios, nossas lash artists dominam essa técnica, "
                "garantindo um resultado elegante e super natural. Se você "
                "quer destacar o olhar, mas sem chamar muita atenção, o Volume "
                "Clássico é a escolha certa pra você!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class SosCapilar(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="Conheça Kesya Heloise, nossa cabeleireira especializada em "
                "protocolos capilares e alinhamentos, utilizando "
                "produtos de alta qualidade como Joico e Vella. Com técnicas "
                "modernas e personalizadas, Kesya transforma seus fios, "
                "garantindo resultados impecáveis e duradouros. "
                "Agende sua consulta e descubra "
                "o poder de um cabelo bem cuidado!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class Cursos(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="No Mundo dos Cílios, além de todos os cuidados que "
                "realçam sua beleza, você também encontra a "
                "oportunidade de transformar sua carreira "
                "com nossos cursos de extensão de cílios e "
                "sobrancelhas. Quer saber mais? É só chamar!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class MinhaAgenda(Screen):
    def __init__(self,**kwargs):
        super(MinhaAgenda, self).__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="No Mundo dos Cílios, além de todos os cuidados que "
                "realçam sua beleza, você também encontra a "
                "oportunidade de transformar sua carreira "
                "com nossos cursos de extensão de cílios e "
                "sobrancelhas. Quer saber mais? É só chamar!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

class RedesSociais(Screen):
    def __init__(self,**kwargs):
        super(RedesSociais, self).__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=20)
        label = MDLabel(
            text="No Mundo dos Cílios, além de todos os cuidados que "
                "realçam sua beleza, você também encontra a "
                "oportunidade de transformar sua carreira "
                "com nossos cursos de extensão de cílios e "
                "sobrancelhas. Quer saber mais? É só chamar!",
            halign="center"
        )
        layout.add_widget(label)
        layout.add_widget(BotaoVoltar())
        self.add_widget(layout)

MundoDosCiliosApp().run()