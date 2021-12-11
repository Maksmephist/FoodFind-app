from kivy.uix.floatlayout import FloatLayout
from plyer import filechooser
from kivy.utils import platform
from kivy.app import App
from food_classificator import FoodClassificator


class ImageChooser(FloatLayout):
    reload_image_timer = None

    def run(self):
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    return
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE], callback)


    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)


    def selected(self, selection):
        if selection:
            food_classif_api = FoodClassificator();
            answer = food_classif_api.get_answer(selection[0])
            App.get_running_app().root.ids.mapview.ids.food_search.text = answer
            App.get_running_app().root.ids.mapview.food_name_input()
            App.get_running_app().root.ids.mapview.start_getting_food_in_fov()

