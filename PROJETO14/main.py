from kivymd.app import MDApp                                # idem a main_0.py
from kivymd.uix.screen import Screen                        # idem a main_0.py
from kivymd.uix.datatables import MDDataTable               # idem a main_1.py
from kivy.metrics import dp                                 # idem a main_1.py
from kivymd.uix.textfield import MDTextField                # idem a main_8.py
from kivymd.uix.boxlayout import MDBoxLayout                # idem a main_8.py
from kivymd.uix.button import MDRaisedButton                # importei a biblioteca que me permite instanciar widgets button


class MainApp(MDApp):                               
    def build(self):                                        # idem a main_0.py

        self.title = "Prof. Saulo Santos | main_9.py"       # idem a main_0.py       

        self.screen = Screen()                              # idem a main_0.py               

        self.tabela = MDDataTable(                          # idem a main_1.py
            pos_hint = {'center_x':0.5,                     # idem a main_3.py
                        'center_y':0.65},                   # idem a main_8.py 
            size_hint=(0.9,0.6),                            # idem a main_6.py
            check = True,                                   # idem a main_6.py
            use_pagination = True,                          # idem a main_6.py
            rows_num = 3,                                   # idem a main_6.py 
            pagination_menu_height = '60dp',                # idem a main_6.py
            column_data = [                                 # idem a main_1.py
                ("ID", dp(20)),
                ("Nome", dp(20)),
                ("Sobrenome", dp(30)),
                ("Email", dp(40)),
                ("Telefone", dp(20))
            ],
            row_data = [                                    # idem a main_6.py
                ("1","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("2","Paulo", "Almeida","paulo@yahoo.com.br","1698789456"),
                ("3","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("4","Paulo", "Almeida","paulo@yahoo.com.br","1698789456"),
                ("5","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("6","Paulo", "Almeida","paulo@yahoo.com.br","1698789456"),
                ("7","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("8","Paulo", "Almeida","paulo@yahoo.com.br","1698789456")
            ]            
        )

        self.tabela.bind(on_check_press = self.checked)     # idem a main_5.py
                                                            # idem a main_5.py     

        self.theme_cls.theme_style = "Light"                # idem a main_0.py
        self.theme_cls.primary_palette = "Orange"           # idem a main_4.py

        self.textfield_codigo = MDTextField(                # idem a main_7.py
            hint_text="Código",                             
            helper_text="Insira o código",                  
            max_text_length=3,                              
            size_hint_x=None,                                
            width=60,                                      
        )                                                   

        self.textfield_nome = MDTextField(
            hint_text="Nome",
            helper_text="Insira o nome",
            max_text_length=50,
        )

        self.textfield_sobrenome = MDTextField(
            hint_text="Sobrenome",
            helper_text="Insira o sobrenome",
            max_text_length=5,
            size_hint_x=None,
            width=200,
        )
        
        self.textfield_email = MDTextField(
            hint_text="Email",
            helper_text="Insira o email",
            max_text_length=50,
        )

        self.textfield_telefone = MDTextField(
            hint_text="Telefone",
            helper_text="Insira o telefone",
            max_text_length=50,
        )

        self.boxLayout1 = MDBoxLayout(spacing="20dp",padding="50dp",pos_hint = {'center_x': 0.5,'center_y':0.65})    # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_codigo)   # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_nome)     # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_sobrenome)# idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_email)    # idem a main_8.py    
        self.boxLayout1.add_widget(self.textfield_telefone) # idem a main_8.py


        adicionar_button = MDRaisedButton(text="Adicionar") # Assim como foi feito com o textfield, estou adicionando 3 buttons
        atualizar_button = MDRaisedButton(text="Adicionar") # Um para incluir, outro para eliminar e outro para alterar registros
        eliminar_button = MDRaisedButton(text="Eliminar")

        self.boxLayout2 = MDBoxLayout(spacing="20dp", padding="50dp")   # Estou criando um segundo BoxLayout para 'jogar' os botões dentro dele     
        self.boxLayout2.add_widget(adicionar_button)        # adicionando botão ao BoxLayout2
        self.boxLayout2.add_widget(atualizar_button)        # adicionando botão ao BoxLayout2
        self.boxLayout2.add_widget(eliminar_button)         # adicionando botão ao BoxLayout2



        self.screen.add_widget(self.tabela)                 # idem a main_1.py
        self.screen.add_widget(self.boxLayout1)             # idem a main_8.py
        self.screen.add_widget(self.boxLayout2)             # Estou adicionando o BoxLayout2 dentro do screen

        return self.screen                                  # idem a main_0.py


    def checked(self, tabela, linha):                       # idem a main_5.py 
        print('tabela: ',tabela, ' linha: ',linha)          # idem a main_5.py
                                                            # idem a main_5.py

    
MainApp().run()                                             # idem a main_0.py