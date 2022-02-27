from kivymd.uix.screen import MDScreen
from AppLocacao.helpackages.helpackages import *


class LoginScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__()
        self.time = 0
        #self.welcome()

    def on_pre_enter(self):
        #  <---- Linhas para busca de horario e retorna ao usuario uma saudação -- Muda o texto Saudação Tela de Login
        self.time = get_time()
        if 5 <= self.time < 12:
            self.ids.welcome_label.text = 'Bom dia!'
        elif 12 <= self.time < 18:
            self.ids.welcome_label.text = 'Boa tarde!'
        else:
            self.ids.welcome_label.text = 'Boa Noite!'

