# FoodFind-app

Обученную модель нейросети [здесь](https://drive.google.com/file/d/1KxqUq75cYWYXgI3lyZMTOPidtimLdxsm/view?usp=sharing).

server.py - с помощью этого файла поднимаю локальный сервер на своем ПК, для которого на flask написал простенькое API, с его помощью приложение на телефоне прокидывает мне на пк изображение, кодируя его в base64, после оно декодируется и нейросеть прогнозирует класс блюда на фото, а пользователю приходит ответ.

Apk файле собирается с помощью [buildozer](https://github.com/kivy/buildozer).

Т.к. на данном этапе проект всё ещё в сыром виде он не доступен в play market, но зато apk файл можно скачать [тут](https://drive.google.com/file/d/1YH-ahbexuH3XuT0gQ_m3iy_m8RYHCKGr/view?usp=sharing).
