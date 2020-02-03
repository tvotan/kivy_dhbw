import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


# Grids with items like columns, rows
class MyGrid():
    name = ObjectProperty(None)
    email = ObjectProperty(None)


class FiveApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    FiveApp().run()
