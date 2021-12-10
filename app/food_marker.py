from kivy_garden.mapview import MapMarkerPopup
from place_popup_info import InfoMenu

class FoodMarker(MapMarkerPopup): 
    place_data = []

    def on_release(self):
        menu = InfoMenu(self.place_data)
        menu.open()
