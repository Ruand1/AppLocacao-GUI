from kivymd.uix.screen import MDScreen
from AppLocacao.helpackages.helpackages import *


class NewRegister(MDScreen):
    def __init__(self, **kw):
        super().__init__()
        self.name_user = ''
        self.last_name_user = ''
        self.email_user = ''
        self.password_user = ''
        self.password_confirmation_user = ''

    def on_pre_enter(self):
        pass

    def callback(self):
        self.manager.current = 'loginscreen'

    def register_user(self):
        self.name_user = self.ids.name_user.text
        self.last_name_user = self.ids.last_name_user.text
        self.email_user = self.ids.email_user.text
        self.password_user = self.ids.password_user.text
        self.password_confirmation_user = self.ids.password_confirmation_user.text

        print(self.name_user)
        print(self.last_name_user)
        print(self.email_user)
        print(self.password_user)
        print(self.password_confirmation_user)





