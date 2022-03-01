import json
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
# from AppLocacao.helpackages.helpackages import *


class NewRegister(MDScreen):

    def __init__(self, **kw):
        super().__init__()
        self.user_register = {}
        self.user_register_saved = []
        self.path = App.get_running_app().user_data_dir + '/'
        self.repeat_register = []
        self.dialog = None

    #    def on_pre_enter(self):
    #        pass
    # self.path = App.get_running_app().user_data_dir+'/'

    def callback(self):
        self.manager.current = 'loginscreen'

    def register_user(self):
        self.load()

        for cad in self.user_register_saved:
            if cad['email_user'] not in self.repeat_register:
                self.repeat_register.append(cad['email_user'])

        #print(f' {self.repeat_register} EMAILS') # TESTESSSS
        self.user_register['name_user'] = self.ids.name_user.text
        self.user_register['last_name_user'] = self.ids.last_name_user.text
        self.user_register['email_user'] = self.ids.email_user.text
        self.user_register['password_user'] = self.ids.password_user.text
        self.user_register['password_confirmation_user'] = self.ids.password_confirmation_user.text

        # <---- Validação do registro
        if self.ids.name_user.text == '' or self.ids.last_name_user.text == '' or self.ids.email_user.text == '' or self.ids.password_user.text == '' or self.ids.password_confirmation_user.text == '':
            if not self.dialog:
                self.dialog = MDDialog(text='Oops! Todos os campos precisam ser preenchidos!')
            else:
                self.dialog = MDDialog(text='Oops! Todos os campos precisam ser preenchidos!')
            self.dialog.open()

        else:
            if self.user_register['password_confirmation_user'] != self.user_register['password_user']:
                if not self.dialog:
                    self.dialog = MDDialog(text='Oops! A confirmação de senha não esta correta!', radius=[20, 7, 20, 7])
                else:
                    self.dialog = MDDialog(text='Oops! A confirmação de senha não esta correta!', radius=[20, 7, 20, 7])
                self.dialog.open()

            else:
                if self.user_register['email_user'] in self.repeat_register:
                    if not self.dialog:
                        self.dialog = MDDialog(text='Este email ja esta cadastrado.', radius=[20, 7, 20, 7])
                    else:
                        self.dialog = MDDialog(text='Este email ja esta cadastrado.', radius=[20, 7, 20, 7])
                    self.dialog.open()
                else:
                    self.user_register_saved.append(self.user_register.copy())
                    self.save()
                    if not self.dialog:
                        self.dialog = MDDialog(text='Cadastro realizado.', radius=[20, 7, 20, 7])
                    else:
                        self.dialog = MDDialog(text='Cadastro realizado.', radius=[20, 7, 20, 7])
                    self.dialog.open()
                    self.manager.current = 'loginscreen'

                    self.ids.name_user.text = ''
                    self.ids.last_name_user.text = ''
                    self.ids.email_user.text = ''
                    self.ids.password_user.text = ''
                    self.ids.password_confirmation_user.text = ''

    def save(self):
        with open(self.path + 'data.json', 'w') as data:
            json.dump(self.user_register_saved, data)

    def load(self, *args):
        try:
            with open(self.path + 'data.json', 'r') as data:
                self.user_register_saved = json.load(data)
        except FileNotFoundError:
            pass
