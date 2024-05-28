from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import webbrowser

class Aplicacion(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        boton1 = Button(text="Abrir web")
        web = TextInput(text="...")
        boton1.bind(on_press=lambda a: webbrowser.open_new(web.text))
        layout.add_widget(web)
        layout.add_widget(boton1)
        return layout

    def on_stop(self):
        print("Siga aprendendo!")

if __name__ == "__main__":
    Aplicacion().run()
