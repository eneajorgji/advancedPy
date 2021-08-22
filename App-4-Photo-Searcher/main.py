from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file("frontend.kv")


class FirstScreen(Screen):
    def search_image(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query

        # Get wikipedia page and the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]

        # Download the image
        req = requests.get(image_link)
        image_path = "files/image.jpg"
        with open(image_path, "wb") as file:
            file.write(req.content)

        # Set the image in the Image Widget
        self.manager.current_screen.ids.img.source = image_path


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
