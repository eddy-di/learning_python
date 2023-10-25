from datetime import datetime, timedelta


class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time
        self.duration = duration
        self.end_time = self.calculate_end_time(self.start_time, self.duration)

    @staticmethod
    def calculate_end_time(start_time, duration):
        # Parse the start time and duration
        start_time_obj = datetime.strptime(start_time, '%H:%M')
        duration_parts = duration.split(':')
        duration_obj = timedelta(hours=int(duration_parts[0]), minutes=int(duration_parts[1]))
        # Calculate the end time by adding the duration to the start time
        end_time_obj = start_time_obj + duration_obj
        # Format the end time as 'HH:MM'
        end_time = end_time_obj.strftime('%H:%M')
        return end_time
    
class Conference:
    def __init__(self):
        self.data = []
        self.data_in_minutes = []
        self.sets = []


    def add(self, new_lecture: Lecture):
        if self.data == []:
            res = (new_lecture.start_time, new_lecture.duration)
            res_mins = (self.convert_to_minutes(new_lecture.start_time), self.convert_to_minutes(new_lecture.duration))
            res_set = set([j+res_mins[0] for j in range(res_mins[1])])
            self.data.append(res)
            self.data_in_minutes.append(res_mins)
            self.sets.append(res_set)
        else:
            new_time_set = self.new_time_set(new_lecture)
            if self.check_time_intersections(new_time_set, self.sets) and self.sets != []:
                raise ValueError('Провести выступление в это время невозможно')
            else:
                res = (new_lecture.start_time, new_lecture.duration)
                res_mins = (self.convert_to_minutes(new_lecture.start_time), self.convert_to_minutes(new_lecture.duration))
                res_set = set([j+res_mins[0] for j in range(res_mins[1])])
                self.data.append(res)
                self.data_in_minutes.append(res_mins)
                self.sets.append(res_set)

    def total(self):
        total_hours = 0
        total_minutes = 0
        for time_str in [i[1] for i in self.data]:
            hours, minutes = map(int, time_str.split(':'))
            total_hours += hours
            total_minutes += minutes
        total_hours += total_minutes // 60
        total_minutes %= 60
        return f"{total_hours:02d}:{total_minutes:02d}"
    
    def longest_lecture(self):
        durations_mapped = [tuple(map(int, i[1].split(':'))) for i in self.data]
        durations_minutes = tuple(map(lambda x: x[0]*60 + x[1], durations_mapped))
        durations_longest = max(durations_minutes)
        longest_hour  = durations_longest // 60 
        longest_minute = durations_longest % 60
        return f"{longest_hour:02d}:{longest_minute:02d}"
    
    def longest_break(self):
        difference = []
        data_min_start_end = sorted([(i[0], i[0]+i[1]) for i in self.data_in_minutes])
        for i in range(len(data_min_start_end)-1):
                difference.append(data_min_start_end[i+1][0] - data_min_start_end[i][1])
        longest_break_min = max(difference)
        return self.convert_to_hour(longest_break_min)

    
    @staticmethod
    def convert_to_minutes(time_str):
        hour_min_int = tuple(map(int, time_str.split(':')))
        hours_to_min = hour_min_int[0] * 60
        return hours_to_min + hour_min_int[1]
    
    @staticmethod
    def convert_to_hour(num_min):
        hour = num_min // 60
        minute = num_min % 60
        return f'{hour:02d}:{minute:02d}'
    
    @staticmethod
    def new_time_set(new_lecture_time: Lecture):
        start = tuple(map(int, new_lecture_time.start_time.split(':')))
        start_minutes = start[0] * 60 + start[1]
        duration = tuple(map(int, new_lecture_time.duration.split(':')))
        duration_minutes = duration[0] * 60 + duration[1]
        return set([i + start_minutes for i in range(duration_minutes)])
    
    @staticmethod
    def check_time_intersections(set_to_check, set_list):
        for s in set_list:
            if not s.isdisjoint(set_to_check):
                return True
        return False
        

        

    
# tests

print('TEST_1:')
conference = Conference()

conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

print('TEST_2:')
conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))

try:
    conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))
except ValueError as error:
    print(error)

print('TEST_3:')
conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:00', '02:00'))

try:
    conference.add(Lecture('Муравьиный алгоритм', '10:00', '04:00'))
except ValueError as error:
    print(error)

print('TEST_4:')
conference = Conference()
conference.add(Lecture('Муравьиный алгоритм', '09:30', '02:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:45', '04:00'))
conference.add(Lecture('Простые числа', '08:00', '01:30'))

print(conference.longest_lecture())
print(conference.longest_break())

print('TEST_5:')
conference = Conference()
conference.add(Lecture('Введение в ООП', '09:30', '00:30'))
conference.add(Lecture('Атрибуты объектов и классов', '08:00', '01:30'))
conference.add(Lecture('Методы экземляра класса', '10:30', '02:00'))

print(conference.longest_lecture())
print(conference.longest_break())

print('TEST_6:')
conference = Conference()
conference.add(Lecture('Декоратор @property', '09:30', '00:30'))
conference.add(Lecture('Свойства', '09:00', '00:30'))
conference.add(Lecture('Модификаторы доступа и аксессоры', '08:30', '00:30'))

print(conference.longest_lecture())
print(conference.longest_break())

print('TEST_7:')
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:30', '00:30'))
except ValueError as e:
    print(e)

print('TEST_8:')
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:45', '00:30'))
except ValueError as e:
    print(e)

print('TEST_9:')
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:59', '00:30'))
except ValueError as e:
    print(e)

print('TEST_10:')
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:35'))
except ValueError as e:
    print(e)

print('TEST_11:')
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))

start_times = ['09:30', '09:45', '09:59', '09:00', '09:00', '09:15', '09:29', '08:30', '11:00', '11:15', '11:25', '10:45']
durations = ['00:30', '00:30', '00:30', '00:35', '00:15', '00:15', '00:30', '00:35', '00:20', '00:10', '00:35', '00:16']

for start_time, duration in zip(start_times, durations):
    try:
        conference.add(Lecture('Строковое представление объектов', start_time, duration))
    except ValueError as e:
        print(e)

print('TEST_12:')
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))
conference.add(Lecture('Унарные операторы и функции', '10:45', '00:15'))
conference.add(Lecture('Арифметические операции', '10:00', '00:30'))
conference.add(Lecture('Вызываемые объекты', '08:00', '01:00'))

print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())


