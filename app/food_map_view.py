from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from food_marker import FoodMarker


class FoodMapView(MapView):
    getting_food_timer = None
    places_names = []
    markers_lst = []
    search_str = ''
    def start_getting_food_in_fov(self):
        #After one second get food in the field of view
        try:
            self.getting_food_timer.cancel()
        except:
            pass
        self.getting_food_timer = Clock.schedule_once(self.get_food_in_fov, 1)
    
    def food_name_input(self):
        return str(self.food_search.text)

    def get_food_in_fov(self, *args):
        try:
            app =  App.get_running_app()
            api_key = 'b4ba53d3-fd7d-4194-93b8-0c96b2c0f76b'
            text = self.food_name_input()
            if text != self.search_str: self.remove_markers()
            self.search_str = text
            bbox = list(map(str, self.get_bbox()))
            url = f'https://search-maps.yandex.ru/v1/?apikey={api_key}&lang=ru_RU&text={text}&bbox={bbox[1]},{bbox[0]}~{bbox[3]},{bbox[2]}'
            if text: self.req = UrlRequest(url, self.add_food_to_map)
        except:
            pass          

    def add_food_to_map(self, *args):
            places = []
            try:
                api_answer = self.req.result['features']
                for place in api_answer:
                    places.append([place['geometry']['coordinates'], place['properties']['CompanyMetaData']['name'],
                                     place['properties']['CompanyMetaData']['address'], place['properties']['CompanyMetaData']['Hours']['text']])
                for place in places:
                    name = place[1]
                    if name in self.places_names:
                        pass   
                    else:
                        self.add_on_map(place)
            except:
                pass

    def add_on_map(self, place):
        lat, lon = place[0][1], place[0][0]
        marker = FoodMarker(lat=lat, lon=lon, source='marker.png')
        self.add_widget(marker)
        marker.place_data = place
        name = place[1]
        self.places_names.append(name)
        self.markers_lst.append(marker)

    def remove_markers(self):
        for i in range(len(self.markers_lst)):
            self.remove_widget(self.markers_lst[i])
        self.markers_lst = []