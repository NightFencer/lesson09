from pprint import pprint
from tkinter.filedialog import askdirectory

# Importing required libraries.
from tkinter import Tk
import os
import hashlib
from pathlib import Path

from PIL import Image, ImageChops

# We don't want the GUI window of
# tkinter to be appearing on our screen
Tk().withdraw()

# Dialog box for selecting a folder.
file_path = askdirectory(title="Select incoming folder ")
print(file_path)
print(len(os.listdir(file_path)))
# Listing out all the files
# inside our root folder.
list_of_files = os.walk(file_path)

# In order to detect the duplicate
# files we are going to define an empty dictionary.
unique_files = dict()

for root, folders, files in list_of_files:

    # Running a for loop on all the files
    for file in files:

        # Finding complete file path
        file_path = Path(os.path.join(root, file))

        # Converting all the content of
        # our file into md5 hash.
        Hash_file = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()

        # If file hash has already #
        # been added we'll simply delete that file
        if Hash_file not in unique_files:
            unique_files[Hash_file] = file_path
        else:
            os.remove(file_path)
            print(f"{file_path} has been deleted")


path = file_path
path = os.path.dirname(path)
print(path)# Путь к папке где лежат файлы для сравнения
imgs = os.listdir(path)

print(imgs)

check_file = 0  # Проверяемый файл
current_file = 0  # Текущий файл

matches_number =0
def difference_images(img1, img2):
    global matches_number
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    size = (30,30)
    image_1.thumbnail(size)
    image_2.thumbnail(size)

    result = ImageChops.difference(image_1, image_2).getbbox()
    if result is None:
        matches_number +=1
        print(img1, img2, 'matches',matches_number)
    return


while check_file < len(imgs):
    if current_file == check_file:
        current_file += 1
        continue
    if current_file == len(imgs):
        break
    print(check_file,current_file)
    difference_images(os.path.join(path,imgs[current_file]), os.path.join(path,imgs[check_file]))
    current_file += 1
    if current_file == len(imgs):
        check_file += 1
        current_file = check_file
