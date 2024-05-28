from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import webbrowser
def msg():
        print("Sigue aprendiendo en : https://inteligencia-artificial.dev/formacion")
class Aplicacion(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        boton1 = Button(text="Abrir web")
        web = TextInput(text="...")
        boton1.bind(on_press= lambda a: webbrowser.open_new(web.text))
        layout.add_widget(web)
        layout.add_widget(boton1)
        return layout
Aplicacion().run()
msg()