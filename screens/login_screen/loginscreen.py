import json
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from AppLocacao.helpackages.helpackages import *


class LoginScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__()
        self.time = 0
        self.user_register_saved = []
        self.path = App.get_running_app().user_data_dir + '/'
        self.repeat_register_email = []
        self.repeat_register_password = []
        self.dialog = None
        self.email_verify = ''

    def on_pre_enter(self):
        #  <---- Linhas para busca de horario e retorna ao usuario uma saudação -- Muda o texto Saudação Tela de Login
        self.time = get_time()
        if 5 <= self.time < 12:
            self.ids.welcome_label.text = 'Bom dia!'
        elif 12 <= self.time < 18:
            self.ids.welcome_label.text = 'Boa tarde!'
        else:
            self.ids.welcome_label.text = 'Boa Noite!'

    def validate_login(self):
        self.load()

        for cad in self.user_register_saved:
            if cad['email_user'] not in self.repeat_register_email:
                self.repeat_register_email.append(cad['email_user'])
            if cad['password_user'] not in self.repeat_register_password:
                self.repeat_register_password.append(cad['password_user'])

        # <---- SE O EMAIL DO USUARIO NÃO ESTIVER NO CADASTRO - GERA POPUP
        if self.ids.email_user.text not in self.repeat_register_email:
            self.dialog = MDDialog(text='Oops! Email não Cadastrado!')
            self.dialog.open()
        # <---- SE O EMAIL ESTIVER NO CADASTRO - DEVEMOS PUXAR A SENHA
        # VERIFICAR PUXAR A POSIÇÃO DO EMAIL DA LISTA
        else:
            self.email_verify = self.repeat_register_email.index(self.ids.email_user.text)
            if self.ids.password_user.text == self.repeat_register_password[self.email_verify]:
                #self.dialog = MDDialog(text='Email Encontrado!')
                #self.dialog.open()
                self.manager.current = 'initialscreen'
            else:
                self.dialog = MDDialog(text='Senha Incorreta!')
                self.dialog.open()

    def load(self, *args):
        try:
            with open(self.path + 'data.json', 'r') as data:
                self.user_register_saved = json.load(data)
        except FileNotFoundError:
            pass


    # Puxar o cadastro dos emails e senhas cadastrados.
    # Bater senha com login
