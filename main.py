#coding=utf-8

import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager

class MyLayout(BoxLayout):
    pass

class MainApp(App):
    theme_cls = ThemeManager()
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return MyLayout()
    def on_start(self):
        self.root.ids.text_input.text='opencv-python version is '+str(cv2.__version__)

MainApp().run()
