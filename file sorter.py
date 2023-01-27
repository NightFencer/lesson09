import datetime
import os
import shutil
import stat
import zipfile
from tkinter import Tk
from tkinter.filedialog import askdirectory
from exif import Image
import ffmpeg


class FileSorter:
    def __init__(self, inbound_folder, out_path, option='replace'):
        self.inbound_folder = inbound_folder  # входящая папка
        self.out_path = out_path  # выходная папка
        self.option = option  # выбор перенос или копирование
        self.file_name = None  # старое имя файла
        self.suffix = None
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
        self.counter = 0
        self.total_removed = 0

    def starter(self):
        self.path_normalaser()
        self.folder_observer()
        print(f'Всего перенесено - {self.counter}, всего удалено - {self.total_removed}')

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
        video_suffixs = ['.MOV', '.m4v', '.mp4', '.MTS', '.3GP', '.MP4', '.mov', '.3gp', '.MOD', '.avi', '.AVI', '.MPG']
        photo_suffixs = ['.JPG', '.jpg', '.CR2']
        suffixs_to_delete =['.AAE','modd','moff','.THM']

        # for dirpath, dirnames, filenames in os.walk('icons'):
        #     for filename in filenames:
        #         file_path = os.path.join(dirpath, filename)

        for dirpath, dirnames, filenames in os.walk(self.inbound_folder):
            for self.file_name in filenames:
                self.suffix = self.file_name[-4:]
                # if self.file_name.endswith('zip'):
                #     self.unzip()
                if self.suffix in suffixs_to_delete:
                    self.full_file_name = os.path.join(dirpath, self.file_name)
                    os.remove(self.full_file_name)
                    print('6')
                if not self.suffix in photo_suffixs:
                    if not self.suffix in video_suffixs:
                        continue
                self.full_file_name = os.path.join(dirpath, self.file_name)
                self.getting_create_time()
                if self.suffix in photo_suffixs:
                    if os.path.getsize(self.full_file_name) > 100000000:
                        print(
                            f'{self.full_file_name} имеет размер более 100Мб, что не харакатерно для фото, он остался на месте')
                        continue
                    self.getting_photo_taking()

                if self.suffix in video_suffixs:
                    self.getting_video_taking()

                if not os.path.isdir(self.full_out_path):
                    os.makedirs(self.full_out_path)
                try:
                    print(self.new_name)
                    shutil.move(self.full_file_name, self.full_out_new_name)
                    self.counter += 1
                    print(f'{self.counter:>5} {self.full_file_name} -->{self.full_out_path} -->{self.new_name}')
                except FileExistsError:
                    self.total_removed += 1
                    print(f'{self.full_file_name} удален как повторный {self.total_removed}')
                    os.remove(self.full_file_name)
                except PermissionError:
                    print(f'{self.full_file_name} не перемещен, а скопирован')
                    shutil.copy2(self.full_file_name, self.full_out_new_name)

            if not os.listdir(dirpath):
                os.chmod(dirpath, stat.S_IWRITE)
                os.rmdir(dirpath)
                print(1)

                # self.new_name = self.new_name[0:-4] + f'({count}).JPG'
                # self.full_out_new_name = os.path.join(self.full_out_path, self.new_name)
                # os.rename(self.full_file_name, self.full_out_new_name)

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
        #print(self.creating_file_date)
        print(self.full_file_name)
        self.creating_file_year = str(self.creating_file_date.year)
        self.creating_file_month = str(self.creating_file_date.month)
        pass

    def getting_photo_taking(self):
        with open(self.full_file_name, 'rb') as image_file:
            file = Image(image_file)
            try:
                self.photo_taking_date = file.get('datetime_original')
            except:
                self.photo_taking_date = None

            if self.photo_taking_date is None:
                self.full_out_path = os.path.join(self.out_path, 'Фото', 'Unable to determine',
                                                  self.creating_file_year, self.creating_file_month)
                self.new_name = self.file_name
                self.full_out_new_name = os.path.join(self.full_out_path, self.new_name)
            else:

                self.photo_taking_year = self.photo_taking_date[0:4]
                self.photo_taking_month = self.photo_taking_date[5:7]
                self.new_name = self.photo_taking_date[8:10] + self.photo_taking_date[11:13] \
                                + self.photo_taking_date[14:16] + self.photo_taking_date[17:19] + self.file_name
                self.full_out_path = os.path.join(self.out_path, 'Фото', self.photo_taking_year,
                                                  self.photo_taking_month)
                self.full_out_new_name = os.path.join(self.full_out_path, self.new_name)

        pass

    def getting_video_taking(self):
        self.full_out_path = os.path.join(self.out_path, 'Видео', self.creating_file_year, self.creating_file_month)
        # print(self.full_out_path)
        self.creating_file_date = str(self.creating_file_date)
        self.new_name = self.creating_file_date[8:10] + self.creating_file_date[11:13] + self.creating_file_date[
                                                                                         14:16] + self.creating_file_date[
                                                                                                  17:19] + self.file_name
        # print(self.new_name)
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


Tk().withdraw()

incoming = askdirectory(title='Папка для обзора')
os.path.normpath(incoming)
outcoming = 'D:\\Наши Фото и Видео'
fotosort = FileSorter(inbound_folder=incoming, out_path=outcoming)
fotosort.starter()
