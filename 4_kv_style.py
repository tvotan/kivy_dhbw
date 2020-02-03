import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


# Grids with items like columns, rows
class MyGrid(Widget):
    pass


# my.kv
# die .kv-File muss genauso heißen wie die class, die build enthaelt, ausgenommen sie endet auf "App", dann muss der Praefix von "App" verwendet werden; lower-cases
# // expand the window
class FourApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    FourApp().run()

