import json
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
# from AppLocacao.helpackages.helpackages import *


class InitialScreen(MDScreen):

    def __init__(self, **kw):
        super().__init__()

    def callback(self):
        self.manager.current = 'loginscreen'
