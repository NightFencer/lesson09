# -*- coding: utf-8 -*-
import datetime
import os, time, shutil
import zipfile

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
# nihuaneponyal
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
in_folder = 'C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\pythonProject\\lesson09\\icons'
in_folder = 'C:\Users\DellWorkStation\Pictures — копия'
os.path.normpath(in_folder)
# print(os.path.dirname(p=in_folder))
i = 1
# zfile = zipfile.ZipFile('icons.zip', 'r')
# for filename in zfile.namelist():
#     zfile.extract(filename)
for dirpath, dirnames, filenames in os.walk(in_folder):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)

        create_time_in_epoha = os.path.getctime(file_path)
        create_time = datetime.datetime.fromtimestamp(create_time_in_epoha)
        year_folder = str(create_time.year)
        month_folder = str(create_time.month)
        # new_folder = os.path.join('c:\\Python\\Tempo',        year_folder, month_folder)
        new_folder = os.path.join('c:\\Python\\Tempo', year_folder, month_folder)
        if not os.path.isdir(new_folder):
            os.makedirs(new_folder)
        print(file_path, f'{year_folder}    {month_folder}    {new_folder}')
        shutil.copy2(file_path, new_folder)

        # os.mkdir()
    # print(dirnames)
    # path=
    # for filename in filenames:
    #     file = filename
    #     c_time= os.path.getctime(filename)
    #     print(filename,i,c_time)
    #     i+=1
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
