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
in_folder = 'C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\pythonProject\\'

for file in files:
    fullfile =os.path.join(in_folder,'lesson09\\tempo',file)

    im = Image.open(fullfile)
    exif = im.getexif()
    creation_time = exif.get(306)
    print(file, exif.get(306))

fullfile ='C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\pythonProject\\lesson09\\tempo\\IMG_8289_254445.jpg'
fullfile1 ='C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\'
fullfile2 ='pythonProject\\pythonProject\\lesson09\\tempo\\accessories-calculator.png'
fullfile = os.path.join(fullfile1,fullfile2)
im = Image.open(fullfile)
print(im.getexif().get(306))
y,m = str(im.getexif().get(306))[0:4],str(im.getexif().get(306))[5:7]
#creation_time = exif.get(306)
print(f'{y}-year, {m}-month')
