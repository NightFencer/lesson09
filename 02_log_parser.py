# -*- coding: utf-8 -*-
import time

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
file_for_check = 'events.txt'


# TODO здесь ваш код
class NokCounter:
    def __init__(self, file_name, observing_period='minute'):
        self.file_name = file_name
        self.observing_period = observing_period
        self.event_number_in_period = 0
        self.current_period = None
        self.previous_period = None
        self.time_parameter = None
        self.line = None
        self.i = None

    def reading_lines(self):


        with open(self.file_name, 'r') as file:
            for line in file:
                self.line = line
                self.finding_period()
                self.current_period = self.time_parameter

                self.event_counter()



    def finding_period(self):
        i = time.strptime(self.line[1:27], '%Y-%m-%d %H:%M:%S.%f')
        self.i = i
        if self.observing_period == 'minute':
            self.time_parameter = i.tm_min
        elif self.observing_period == 'hour':
            self.time_parameter = i.tm_hour
        elif self.observing_period == 'month':
            self.time_parameter = i.tm_mon
        elif self.observing_period == 'day':
            self.time_parameter = i.tm_mday
        else:
            self.time_parameter = i.tm_year

    def write_event(self):
        #print(self.current_period,self.event_number_in_period,'----------')
        print(f'[{self.i.tm_year}-{self.i.tm_mon}-{self.i.tm_mday} {self.i.tm_hour}:{self.i.tm_min}]  {self.event_number_in_period}')
        print(self.previous_period, self.event_number_in_period, '+++')
        pass

    def event_counter(self):
        #print(self.previous_period,self.current_period,self.event_number_in_period,'---')

        if self.previous_period != self.current_period:
            if not self.previous_period == None:
                #print(self.previous_period, self.event_number_in_period, '---')
                self.write_event()
            self.event_number_in_period = 0

        if event in self.line:
            self.event_number_in_period += 1

        #print(self.previous_period, self.current_period, self.event_number_in_period, '+++',self.line[-4:-1])

        self.previous_period = self.current_period

        pass


# открыть файл
#
# прочитать строку
# определить минуту
# посчитать НОК
# записать в файл
period = 'minute'
event = 'NOK'
counter = NokCounter(file_name=file_for_check, observing_period=period)
counter.reading_lines()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
