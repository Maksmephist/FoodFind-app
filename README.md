# FoodFind-app

Ссылка на обученную модель нейросети: https://drive.google.com/file/d/1KxqUq75cYWYXgI3lyZMTOPidtimLdxsm/view?usp=sharing

server.py - с помощью этого файла поднимаю локальный сервер на своем ПК, для которого на flask написал простенькое API, с его помощью приложение на телефоне прокидывает мне на пк изображение, кодируя его в base64, после оно декодируется и нейросеть прогнозирует класс блюда на фото, а пользователю приходит ответ.

Apk файле комплируется с помощью [buildozer](https://github.com/kivy/buildozer)
