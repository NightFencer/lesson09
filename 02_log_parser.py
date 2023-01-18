# -*- coding: utf-8 -*-
from time import strptime


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

# TODO здесь ваш код
class LogEventCounter:
    def __init__(self, file_name, out_file_name):
        self.event_for_find = None
        self.file_name = file_name
        self.out_file_name = out_file_name
        self.observing_period_name = None
        self.time_parameters = None
        self.observing_period_parameter = None
        self.opened_period = None
        self.closed_period = False
        self.file_line = None
        self.file_checked_line = None
        self.line_lenth= 0
        self.event_number_in_current_period = 0

    def getting_period_for_count(self):
        if self.observing_period_name == 'minute':
            self.observing_period_parameter = self.time_parameters.tm_min
            self.line_lenth = 17

            pass
        elif self.observing_period_name == 'hour':
            self.observing_period_parameter = self.time_parameters.tm_hour
            self.line_lenth = 14
            pass
        elif self.observing_period_name == 'month':
            self.observing_period_parameter = self.time_parameters.tm_mon
            self.line_lenth = 8
        elif self.observing_period_name == 'day':
            self.observing_period_parameter = self.time_parameters.tm_mday
            self.line_lenth = 11

            pass
        else:
            self.observing_period_parameter = self.time_parameters.tm_year
            self.line_lenth = 5
            pass

    def event_count(self):
        if self.opened_period is None:
            self.opened_period = self.observing_period_parameter

        if not self.opened_period == self.observing_period_parameter:
            self.closed_period = True
            self.printing_event_number()
            self.event_number_in_current_period = 0
            self.opened_period = self.observing_period_parameter

        if self.event_for_find in self.file_line:
            self.event_number_in_current_period += 1



    def printing_event_number(self):
        if self.closed_period ==True:
            result =f'{self.file_checked_line[:self.line_lenth]}] {self.event_number_in_current_period}'
            print(result)

            with open(self.out_file_name,'a', encoding='utf8') as out_file:

                out_file.write(result+'\n')

        pass


    def reading_file(self,observing_period_name='minute'):
        self.observing_period_name = observing_period_name
        with open(self.file_name, 'r') as file:
            for line in file:
                self.file_line = line
                self.time_parameters = strptime(self.file_line[1:26], format)
                self.getting_period_for_count()

                self.event_count()

                self.file_checked_line = line
            if not self.closed_period:
                self.closed_period =True
                self.printing_event_number()
    def count_event(self,period = 'minute',event =''):
        open(self.out_file_name, 'w').close()
        self.event_for_find=event
        self.reading_file(period)



file_name = 'events.txt'
out_file_name = 'out_log.txt'
format = '%Y-%m-%d %H:%M:%S.%f'
period = 'minute'
#period = 'hour'
# period = 'month'
# period = 'year'
# period = 'day'
event = ' NOK'
nok_counter = LogEventCounter(file_name,out_file_name)
nok_counter.count_event(event=event,period=period)
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
