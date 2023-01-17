# -*- coding: utf-8 -*-
import os
import zipfile
from pprint import pprint

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
file_path = 'C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\pythonProject\\lesson09\\python_snippets\\voyna-i-mir.txt.zip'
# file_path = 'C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\pythonProject\\lesson09\\voyna-i-mir.txt'
# file_path = "C:\\Users\\DellWorkStation\\Desktop\\22\\tested2.txt"
print(os.path.getsize(file_path))


class Statistic:
    def __init__(self, file_name):
        self.sorted_keys = None
        self.file_name = file_name
        self.stat = {}
        self.stat_sorted = {}

    def sort_min_to_max(self):

        self.sorted_keys = sorted(self.stat, key=self.stat.get, reverse=False)
        for i in self.sorted_keys:
            self.stat_sorted[i] = self.stat[i]

    def sort_max_to_min(self):
        self.sorted_keys = sorted(self.stat, key=self.stat.get, reverse=True)
        for i in self.sorted_keys:
            self.stat_sorted[i] = self.stat[i]

        pass
    def sort_A_to_Z(self):
        #global e_index, yo_pair
        pairs = sorted(self.stat.items(), reverse= False)
        for i in range(len(pairs)):


            if pairs[i][0] == 'е':
                e_index = i
            if pairs[i][0] == 'ё':
                yo_pair = pairs[i]

        pairs.insert(e_index+1,yo_pair)
        for pair in pairs:

            self.stat_sorted[pair[0]]=pair[1]
        pass
    def sort_Z_to_A(self):
        pairs = sorted(self.stat.items(), reverse=True)
        for i in range(len(pairs)):
            j=0
            if pairs[i][0] == 'ё':
                yo_pair = pairs[i]
                yo_index= i
                j+=1

            if pairs[i][0] == 'е':
                e_index = i
                j+=1
            if j==2:
                break

        pairs.pop(yo_index)
        pairs.insert(e_index-1 , yo_pair)
        for pair in pairs:
            self.stat_sorted[pair[0]] = pair[1]
        pass


    def print_statistic(self):
        self.get_letters_number()
        form = ['+'+'-'*15+'+'+'-'*15+'+','статистика букв','+'+'-'*15+'+'+'-'*15+'+']
        for line in form:
            if len(line)== 33:
                print(line)
            else:
                print(f'|{line:^31}|')
        txt1,txt2 = 'буква','частота'
        print(f'|{txt1: ^15}|{txt2: ^15}|')
        print(form[0])
        #self.sort_min_to_max()
        #self.sort_max_to_min()
        #self.sort_A_to_Z()
        self.sort_Z_to_A()


        for letter, frequency in self.stat_sorted.items():
        #for letter, frequency in self.stat.items():
            print(f'|{letter: ^15}|{frequency: ^15}|')
        print(form[0])


    def get_letters_number(self):

        self.getting_file()
        self.collecting()


    def unzip(self):
        print(self.file_name)

        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
            self.file_name = os.path.abspath(filename)

    def getting_file(self):
        if file_path.endswith('zip'):
            self.unzip()
        else:
            print(self.file_name)

    def collecting(self):
        # with open(self.file_name, 'r', encoding='cp1251') as file:
        with open(self.file_name, 'r') as file:
            print(file.closed)
            for line in file:
                self.collecting_line(line=line)
        print(file.closed)

    def collecting_line(self, line):

        for char in line:

            if char.isalpha():
                if not char in self.stat:
                    self.stat[char] = 1
                else:
                    self.stat[char] += 1


statistic = Statistic(file_name=file_path)
#statistic.sort_A_to_Z()
statistic.print_statistic()
