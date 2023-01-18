import os
from PIL import Image
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
#     print(dateTaken)
in_folder = 'C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\pythonProject\\lesson09\\tempo'
files = os.listdir(in_folder)
for file in files:
    fullfile =os.path.join(in_folder,file)
    im = Image.open(fullfile)
    exif = im.getexif()
    creation_time = exif.get(306)
    print(file, exif.get(306))
