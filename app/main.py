from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.network.urlrequest import UrlRequest
from food_map_view import FoodMapView
from gps_helper import GpsHelper
from image_chooser import ImageChooser


#from kivy.core.window import Window
#Window.size = (375, 650)

Builder.load_file('main.kv')

class AppLayout(Widget):    
    pass
    
    
class FoodFind(MDApp):


    def on_start(self):
        GpsHelper().run()
        

    def build(self):
        return AppLayout()


if __name__ == '__main__':
    FoodFind().run()