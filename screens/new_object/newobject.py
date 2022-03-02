import json
from kivy.app import App
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
# from AppLocacao.helpackages.helpackages import *


class NewObject(MDScreen):

    def __init__(self, **kw):
        super().__init__()
        Window.bind(on_keyboard=self.events)  # Pode ser preciso para Mobile
        self.manager_open = False
        self.path_image = ''
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def callback(self):
        self.manager.current = 'initialscreen'

    def file_manager_open(self):
        # self.file_manager.show_disks() # FUNÇÃO NÃO ESTA FUNCIONANDO - VERIFICAR NECESSIDADE
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        #       '''It will be called when you click on the file name
        #        or the catalog selection button.

        #        :type path: str;
        #        :param path: path to the selected directory or file;
        #        '''
        self.path_image = path
        print(self.path_image)
        self.ids.image_to_pass.source = self.path_image
        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        #        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        #        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
