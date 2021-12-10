from kivymd.uix.dialog import MDDialog


class InfoMenu(MDDialog):
     def __init__(self, place_data):
        super().__init__()
        self.text = place_data[1] + '\n' + place_data[2] + '\n' + place_data[3]
