#from fcntl import F_GETLEASE
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time 

from filesharer import FileSharer

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
       # """starts camera and change Button text"""
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        #"""Stops camera and changes Button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        

    def capture(self):
        #"""Create a filename with the current time and captures and save a photo image under that filename"""
        current_time = time.strftime('%y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'   
        self.manager.current_screen.ids.ing.source = self.filepath
        
class ImageScreen(Screen):
    def create_Link(self):
        ## Access the photo filepath, uploads it to the web, and inserts the link in the label wifdgrt
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath = file_path)
        url = filesharer.share()
        self.ids.link.text = url


      
class RootWidget(ScreenManager):
      pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
