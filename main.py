from kivy.app import App
from kivy.uix.label import Label

class VistaApp(App):
    def build(self):
        return Label(text='Hey Vista App is Working!', font_size='24sp')

if __name__ == '__main__':
    VistaApp().run()
