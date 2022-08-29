from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate Design file
Builder.load_file('menu.kv')

class MyLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:
            pass

class ImageViewApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    ImageViewApp().run()