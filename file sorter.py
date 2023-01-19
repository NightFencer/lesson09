import datetime
import os
import shutil
import zipfile

import PIL.Image


class FileSorter:
    def __init__(self, inbound_folder, out_path, option='replace'):
        self.inbound_folder = inbound_folder  # входящая папка
        self.out_path = out_path  # выходная папка
        self.option = option  # выбор перенос или копирование
        self.out_fullpath = None
        self.file_path = None
        self.file_name = None
        self.photo_taking_date = None
        self.photo_taking_year = None
        self.photo_taking_month = None
        self.creating_file_date_in_epoha = None
        self.creating_file_date = None
        self.creating_file_year = None
        self.creating_file_month = None

    def starter(self):
        self.path_normalaser()
        self.folder_observer()



        pass

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
            self.file_name = filename

        pass

    def path_normalaser(self):
        os.path.normpath(self.inbound_folder)
        pass

    def folder_observer(self):
        for dirpath, dirnames, filenames in os.walk(self.inbound_folder):
            for self.file_name in filenames:
                if self.file_name.endwith('zip'):
                    self.unzip()

                self.file_path = os.path.join(dirpath, self.file_name)
                self.getting_create_time()
                self.getting_photo_taking()
                if not os.path.isdir(self.out_fullpath):
                    os.makedirs(self.out_fullpath)
                shutil.move(self.file_path,self.out_fullpath)
        pass

    def getting_create_time(self):
        self.creating_file_date_in_epoha = os.path.getctime(self.file_path)
        self.creating_file_date = datetime.datetime.fromtimestamp(self.creating_file_date_in_epoha)
        self.creating_file_year = str(self.creating_file_date.year)
        self.creating_file_month = str(self.creating_file_date.month)
        pass

    def getting_photo_taking(self):
        image = PIL.Image.open(self.file_path)
        checking_exif = image.getexif().get(306)
        if not checking_exif is None:

            self.photo_taking_date = str(checking_exif)
            self.photo_taking_year = self.photo_taking_date[0:4]
            self.photo_taking_month = self.photo_taking_date[5:7]
            self.out_fullpath = os.path.join(self.out_path, self.photo_taking_year, self.photo_taking_month)
        else:
            self.out_fullpath = os.path.join(self.out_path, 'Unable to determine',
                                             self.creating_file_year,self.creating_file_month)

        pass

    def new_path_maker(self):
        pass

    def file_checker(self):
        pass

    def file_copier(self):
        pass

    def file_replacer(self):
        pass

    def result_printing(self):
        pass
