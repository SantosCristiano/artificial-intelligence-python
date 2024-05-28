from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from gtts import gTTS
from playsound import playsound

class TextToSpeechApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        self.text_input = TextInput(hint_text='Digite seu texto aqui', multiline=True)
        layout.add_widget(self.text_input)

        play_button = Button(text='Play', size_hint=(1, 0.2))
        play_button.bind(on_press=self.play_text)
        layout.add_widget(play_button)

        return layout

    def play_text(self, instance):
        text = self.text_input.text
        if text.strip():  # Verifica se há texto para ser falado
            file = gTTS(text=text, lang='en')  # 'en' para inglês, substitua pelo idioma desejado
            file.save("voz.mp3")
            playsound("voz.mp3")

if __name__ == '__main__':
    TextToSpeechApp().run()
