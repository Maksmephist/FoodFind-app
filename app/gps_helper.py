from kivy.app import App
from kivy.utils import platform
from plyer import gps
from kivy.clock import Clock


class GpsHelper():
    has_centered_map = False
    blinker_update_timer = None

    def run(self):
        # Get a reference to GpsBlinker, then call blink()
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        # Start blinking the GpsBlinker
        gps_blinker.blink()
        # Request permissions on Android
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    gps.configure(on_location=self.update_blinker_position)
                    gps.start(minTime=1000, minDistance=0)
            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)
        # Configure GPS
        if platform == 'ios':
            gps.configure(on_location=self.update_blinker_position)
            gps.start(minTime=1000, minDistance=0)
         #After one second update blinker position
    
    def update_blinker_position(self, *args, **kwargs):
        my_lat = kwargs['lat']
        my_lon = kwargs['lon']
        # Update GpsBlinker position
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        gps_blinker.lat = my_lat
        gps_blinker.lon = my_lon
        # Center map on gps
        if not self.has_centered_map:
            map = App.get_running_app().root.ids.mapview
            map.center_on(my_lat, my_lon)
            self.has_centered_map = True

