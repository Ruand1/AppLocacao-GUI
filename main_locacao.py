from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
import os
#  from android.permissions import request_permissions, Permission  # PARA RODAR NO DESKTOP COMENTAR ESTA LINHA
import kivy
kivy.require('2.0.0')


class LiveApp(MDApp, App):
    DEBUG = 1

    KV_FILES = {
        os.path.join(os.getcwd(), 'screens/screenmanager.kv'),
        os.path.join(os.getcwd(), 'screens/login_screen/loginscreen.kv'),
        os.path.join(os.getcwd(), 'screens/new_register/newregister.kv'),
        os.path.join(os.getcwd(), 'screens/initial_screen/initialscreen.kv'),
    }

    CLASSES = {
        'MainScreenManager': 'screens.screenmanager',
        'LoginScreen': 'screens.login_screen.loginscreen',
        'NewRegister': 'screens.new_register.newregister',
        'InitialScreen': 'screens.initial_screen.initialscreen',
    }

    AUTORELOADER_PATHS = [
        ('.', {'recursive': True}),
    ]

    def build_app(self, **kwargs):
        self.theme_cls.primary_palette = 'Green'
        return Factory.MainScreenManager()

    def dark_theme(self):
        self.theme_cls.theme_style = 'Dark'

    def light_theme(self):
        self.theme_cls.theme_style = 'Light'

# <---- Quando usamos o icone para fazer duas funções, não executa se muda o botão de posição
    def change_theme(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'


if __name__ == '__main__':
    LiveApp().run()
