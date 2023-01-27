import os.path
from datetime import datetime
from pprint import pprint

import ffmpeg
from PIL import Image, ExifTags


def image_metadata(path_f):
    img = Image.open(path_f)
    info_dict = {
            "Имя файла": os.path.split(path_f)[1],
            "Разрешение изображения": img.size,
            "Высота изображения": img.height,
            "Ширина изображения": img.width,
            "Формат изображения": img.format,
            "Режим изображения": img.mode,
            "Анимированное изображение": getattr(img, "is_animated", False),
            "Кадров в изображении": getattr(img, "n_frames", 1)
        }
    try:
        exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}

        print(f'\n[+] Метаданные фото: {os.path.split(path_f)[1]:27}\n')
        for info in exif:
            if info == 'GPSInfo':
                print(f'{info:27}: lat {exif[info][2]} {exif[info][1]} - long {exif[info][4]} {exif[info][3]}')
            else:
                if isinstance(exif[info], bytes):
                    info_d = exif[info].decode()
                    print(f'{info:25}: {info_d}')
                else:
                    print(f'{info:25}: {exif[info]}')
    except AttributeError:
        print(f'\n[+] Информация о фото: {os.path.split(path_f)[1]:27}\n')
        for k, v in info_dict.items():
            print(f"{k:27}: {v}")
        exit(0)


def vid_aud_matadata(patn_f):
    try:
        print(f'\n[+] Метаданные файла: {os.path.split(patn_f)[-1]}\n')
        pprint(ffmpeg.probe(patn_f)["streams"])
    except ffmpeg._run.Error:
        print('[-] Неподдерживаемый формат')


# if __name__ == "__main__":
#     path_file1 = input('[~] Введите путь к файлу: ')
#     path_file ='C:\\Users\\DellWorkStation\\Videos\\VID_20220713_12063.mp4'
#     if not os.path.exists(path_file):
#         print('[-] Файла не существует')
#     else:
#         if path_file.endswith(".jpg"):
#             image_metadata(path_file)
#         elif path_file.endswith(".jpeg"):
#             image_metadata(path_file)
#         else:
#             vid_aud_matadata(path_file)
path_file ='C:\\Users\\DellWorkStation\\Videos\\VID_20220713_12063.mp4'
cr_time = os.path.getctime(path_file)
md_time = os.path.getmtime(path_file)
if md_time is None:
    creating_file_date_in_epoha = cr_time
elif md_time < cr_time:
    creating_file_date_in_epoha = md_time
else:
    creating_file_date_in_epoha = cr_time

creating_file_date = datetime.fromtimestamp(creating_file_date_in_epoha)
creating_file_year = str(creating_file_date.year)
creating_file_month = str(creating_file_date.month)
print(creating_file_date,creating_file_year,creating_file_month)