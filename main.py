#from fcntl import F_GETLEASE
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time 
#from filesharer import Filesharer


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
        #"""Create a filename with the current time and captures 
        # and save a photo image under that filename"""
        current_time = time.strftime('%y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'   
        self.manager.current_screen.ids.ing.source = self.filepath
        
class ImageScreen(Screen):
      def create_Link(self):
        file_path = App.get_running_ap().root.ids.camera_screen.filepath
        print(file_path)     
      
class RootWidget(ScreenManager):
      pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
