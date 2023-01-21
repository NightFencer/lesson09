import datetime
import os
import shutil
import zipfile
from exif import Image


class FileSorter:
    def __init__(self, inbound_folder, out_path, option='replace'):
        self.inbound_folder = inbound_folder  # входящая папка
        self.out_path = out_path  # выходная папка
        self.option = option  # выбор перенос или копирование
        self.file_name = None  # старое имя файла
        self.new_name = None  # новое имя файла
        self.full_out_path = None  # новая папка назначения с месяцем и годом
        self.full_out_new_name = None  # новое имя файла с полным путем
        self.full_file_name = None  # старое имя файла с путем

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
        count = 0
        for dirpath, dirnames, filenames in os.walk(self.inbound_folder):
            for self.file_name in filenames:
                if self.file_name.endswith('zip'):
                    self.unzip()
                if not self.file_name.endswith('.JPG'):
                    continue

                self.full_file_name = os.path.join(dirpath, self.file_name)
                if os.path.getsize(self.full_file_name) > 100000000:
                    continue
                self.getting_create_time()
                self.getting_photo_taking()
                if not os.path.isdir(self.full_out_path):
                    os.makedirs(self.full_out_path)
                try:
                    os.rename(self.full_file_name, self.full_out_new_name)
                except:


                    self.new_name = self.new_name[0:-4] + f'({count}).JPG'
                    self.full_out_new_name = os.path.join(self.full_out_path, self.new_name)
                    os.rename(self.full_file_name, self.full_out_new_name)

                count += 1
                print(f'{count:>5} {self.full_file_name} -->{self.full_out_path} -->{self.new_name}')
                # shutil.move(self.full_file_name, self.full_out_path)

        pass

    def getting_create_time(self):
        cr_time = os.path.getctime(self.full_file_name)
        md_time = os.path.getmtime(self.full_file_name)
        if md_time is None:
            self.creating_file_date_in_epoha = cr_time
        elif md_time < cr_time:
            self.creating_file_date_in_epoha = md_time
        else:
            self.creating_file_date_in_epoha = cr_time

        self.creating_file_date = datetime.datetime.fromtimestamp(self.creating_file_date_in_epoha)
        self.creating_file_year = str(self.creating_file_date.year)
        self.creating_file_month = str(self.creating_file_date.month)
        pass

    def getting_photo_taking(self):
        with open(self.full_file_name, 'rb') as image_file:
            file = Image(image_file)
            self.photo_taking_date = file.get('datetime_original')
            if self.photo_taking_date is None:
                self.full_out_path = os.path.join(self.out_path, 'Unable to determine',
                                                  self.creating_file_year, self.creating_file_month)
                self.new_name = self.file_name
                self.full_out_new_name = os.path.join(self.full_out_path, self.new_name)
            else:

                self.photo_taking_year = self.photo_taking_date[0:4]
                self.photo_taking_month = self.photo_taking_date[5:7]
                self.new_name = self.photo_taking_date[8:10] + self.photo_taking_date[11:13] \
                                + self.photo_taking_date[14:16] + self.photo_taking_date[17:19] + '.JPG'
                self.full_out_path = os.path.join(self.out_path, self.photo_taking_year, self.photo_taking_month)
                self.full_out_new_name = os.path.join(self.full_out_path, self.new_name)

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


incoming = 'C:\\временная папка\\Pictures\\8.01.16'
outcoming = 'C:\\photo_sorted'
fotosort = FileSorter(inbound_folder=incoming, out_path=outcoming)
fotosort.starter()
