from kivy.app import App
from kivy.uix.label import Label

class SmartDRS(App):
    def build(self):
        return Label(text="Smart DRS App Running 🎉")

if __name__ == "__main__":
    SmartDRS().run()
