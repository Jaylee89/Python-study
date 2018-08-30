# coding: utf-8

"""
sub-classing the App class
implementing its build() method so it returns a Widget instance (the root of your widget tree)
instantiating this class, and calling its run() method.
"""

import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello Kivy')

if __name__ == '__main__':
    MyApp().run()