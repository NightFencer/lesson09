import os
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import TAGS
from pprint import pprint

# path = 'c:\\Windows'
# number =0
# for dirpath,dirnames,filenames in os.walk(path):
#     print(dirpath,dirnames,filenames)
#     print('yohoo!!!!!!')
#     number += len(filenames)
print(__file__)
print(os.path.dirname(__file__))

# with open('image.jpg', 'rb') as fh:
#     tags = EXIF.process_file(fh, stop_tag="EXIF DateTimeOriginal")
#     dateTaken = tags["EXIF DateTimeOriginal"]
# #     print(dateTaken)
# in_folder = 'C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\pythonProject\\lesson09\\tempo'
# files = os.listdir(in_folder)
# in_folder = 'C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\pythonProject\\'




from exif import Image
ff= 'C:\\временная папка\\Pictures\\photo kolya_experiment\\05125028.JPG'
with open(ff, 'rb') as image_file:

    file = Image(image_file)
if (os.path.getsize(ff))>10000000:
    print('file more 10')
elif os.path.getsize(ff)>6000000:
    print('file more 6')
elif os.path.getsize(ff)>5000000:
    print('file more 5')
else:
    print('small')


print(file.get('datetime_original'))
creation_date = file.get('datetime_original')
creation_time = creation_date
y, m = creation_date[0:4], creation_date[5:7]

name = creation_time[8:10] + creation_time[11:13] + creation_time[14:16] + creation_time[17:19] + '.JPG'
print(f'{y:6}--{m:6}---{name}')
