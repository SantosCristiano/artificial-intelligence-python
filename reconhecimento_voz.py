# pip install pipwin
# pip install speechrecognition
# pip install --upgrade speechrecognition
# pip install pyjokes
# pip install requests
# pip install kivy

import webbrowser
import speech_recognition as sr
import time
import os
import pyjokes
import requests
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import mainthread


class VoiceAssistantApp(App):
    def build(self):
        self.title = 'Assistente de Voz Tronic'
        layout = BoxLayout(orientation='vertical')

        self.output_label = Label(size_hint_y=None, text='Olá, sou seu assistente de voz Tronic')
        self.output_label.bind(texture_size=self.output_label.setter('size'))

        self.scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 150))
        self.scrollview.add_widget(self.output_label)

        self.start_button = Button(text='Iniciar Assistente de Voz', size_hint_y=None, height=50)
        self.start_button.bind(on_press=self.start_listening)

        self.stop_button = Button(text='Parar', size_hint_y=None, height=50)
        self.stop_button.bind(on_press=self.stop_listening)
        self.stop_button.disabled = True

        layout.add_widget(self.scrollview)
        layout.add_widget(self.start_button)
        layout.add_widget(self.stop_button)

        return layout

    @mainthread
    def update_output(self, text):
        self.output_label.text += f'\n{text}'
        self.scrollview.scroll_y = 0

    def assistant_response(self, text):
        self.update_output(f'Assistente: {text}')

    def open_website(self, url):
        webbrowser.open(url)
        self.assistant_response(f'Abrindo {url}')

    def tell_joke(self):
        joke = pyjokes.get_joke(language='es')
        self.assistant_response(joke)

    def get_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        self.assistant_response(f'A hora atual é {current_time}')

    def search_google(self, query):
        url = f'https://www.google.com/search?q={query}'
        webbrowser.open(url)
        self.assistant_response(f'Buscando {query} no Google')

    def open_application(self, app_name):
        try:
            if os.name == 'posix':  # macOS or Linux
                os.system(f'open -a "{app_name}"')
            elif os.name == 'nt':  # Windows
                os.system(f'start {app_name}')
            self.assistant_response(f'Abrindo {app_name}')
        except Exception as e:
            self.assistant_response(f'Não posso abrir {app_name}. Erro: {str(e)}')

    def play_music(self, song_name):
        query = f'{song_name} site:youtube.com'
        self.search_google(query)
        self.assistant_response(f'Tocando {song_name} no YouTube')

    def get_weather(self, city):
        api_key = "sua_chave_de_api"
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br"
        response = requests.get(base_url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            description = weather["description"]
            weather_response = f"Está {description} em {city} com temperatura de {temperature}°C"
            self.assistant_response(weather_response)
        else:
            self.assistant_response("Cidade não encontrada")

    def start_listening(self, instance):
        self.stop_button.disabled = False
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.assistant_response('Estou ouvindo...')
            self.recognizer.adjust_for_ambient_noise(source)
            self.audio = self.recognizer.listen(source, timeout=5)

            try:
                text = self.recognizer.recognize_google(self.audio, language="pt-BR")
                self.assistant_response(f'Você disse: {text}')
                self.handle_command(text)
            except sr.UnknownValueError:
                self.assistant_response('Não foi detectado nenhum áudio.')
            except sr.RequestError as e:
                self.assistant_response(f'Erro no serviço de reconhecimento; {e}')

    def stop_listening(self, instance):
        self.recognizer.__exit__()
        self.assistant_response('Parou de ouvir.')

    def handle_command(self, text):
        if "meu site" in text:
            self.open_website('https://teckins.com')
        elif "Amazon" in text:
            self.open_website('https://amazon.com')
        elif "notícias" in text or "news" in text:
            self.open_website('https://news.google.com')
        elif "YouTube" in text:
            self.open_website('http://youtube.com')
        elif "Google" in text:
            self.open_website('http://google.com')
        elif "Facebook" in text:
            self.open_website('http://facebook.com')
        elif "Twitter" in text:
            self.open_website('http://twitter.com')
        elif "Instagram" in text:
            self.open_website('http://instagram.com')
        elif "tudo bem" in text:
            self.assistant_response("Tudo bem e você?")
        elif "piada" in text:
            self.tell_joke()
        elif "hora" in text:
            self.get_time()
        elif "tempo" in text:
            if "previsão do tempo em" in text:
                try:
                    city = text.split("previsão do tempo em", 1)[1].strip()
                    self.get_weather(city)
                except IndexError:
                    self.assistant_response("Por favor, forneça o nome da cidade.")
            else:
                self.assistant_response("Por favor, diga 'previsão do tempo em [cidade]'")
        elif "sair" in text:
            self.assistant_response("Até logo!")
            App.get_running_app().stop()
        elif "buscar" in text:
            try:
                query = text.split("buscar", 1)[1].strip()
                self.search_google(query)
            except IndexError:
                self.assistant_response("Por favor, forneça o termo de busca.")
        elif "abrir" in text:
            try:
                app_name = text.split("abrir", 1)[1].strip()
                self.open_application(app_name)
            except IndexError:
                self.assistant_response("Por favor, forneça o nome do aplicativo.")
        elif "tocar" in text:
            try:
                song_name = text.split("tocar", 1)[1].strip()
                self.play_music(song_name)
            except IndexError:
                self.assistant_response("Por favor, forneça o nome da música.")
        else:
            self.assistant_response("Não entendi. Por favor, tente novamente.")


if __name__ == '__main__':
    VoiceAssistantApp().run()
