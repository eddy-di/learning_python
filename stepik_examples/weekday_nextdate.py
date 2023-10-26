from enum import Enum
from datetime import date, timedelta 


Weekday = Enum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today: date, weekday: Weekday, after_today=False) -> None:
        self.today = today
        self.today_weekday = today.weekday()
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        if not self.after_today:
            if self.weekday.value == self.today_weekday:
                return self.today + timedelta(days=7)
            elif self.weekday.value > self.today_weekday:
                return self.today + timedelta(days=(self.weekday.value - self.today_weekday))
            elif self.weekday.value < self.today_weekday:
                return self.today + timedelta(days=(7 - (self.today_weekday - self.weekday.value)))
        else:
            if self.weekday.value == self.today_weekday:
                return self.today + timedelta(days=0)
            elif self.weekday.value > self.today_weekday:
                return self.today + timedelta(days=(self.weekday.value - self.today_weekday))
            elif self.weekday.value < self.today_weekday:
                return self.today + timedelta(days=(7 - (self.today_weekday - self.weekday.value)))
        

    def days_until(self):
        return (self.date() - self.today).days

        

# tests

# print('TEST_1:')
# from datetime import date
# 
# today = date(2023, 4, 17)                              # понедельник
# next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница
# 
# print(next_friday.date())
# print(next_friday.days_until())
# 
# print('TEST_2:')
# from datetime import date
# 
# today = date(2023, 4, 17)                              # понедельник
# next_monday = NextDate(today, Weekday.MONDAY)          # следующий понедельник без учета текущего
# 
# print(next_monday.date())
# print(next_monday.days_until())
# 
# print('TEST_3:')
# from datetime import date
# 
# today = date(2023, 4, 17)                              # понедельник
# next_monday = NextDate(today, Weekday.MONDAY, True)    # следующий понедельник с учетом текущего
# 
# print(next_monday.date())
# print(next_monday.days_until())
# 
# print('TEST_4:')
# from datetime import date
# 
# for weekday in Weekday:
    # today = date(2023, 4, 27)                              # четверг
    # next_date = NextDate(today, weekday)
# 
    # print(next_date.date())
    # print(next_date.days_until())
# 
# print('TEST_5:')
# from datetime import date
# 
# for weekday in Weekday:
    # today = date(2023, 4, 27)                              # четверг
    # next_date = NextDate(today, weekday, True)
# 
    # print(next_date.date())
    # print(next_date.days_until())
# 
print('TEST_6:')
from datetime import date, timedelta

today = date(2023, 4, 23)

for _ in range(7):
    today += timedelta(days=1)
    for weekday in Weekday:
        next_date = NextDate(today, weekday)
        print(f'Today = {today} {Weekday(today.weekday()).name}, next {weekday.name} = {next_date.date()}')
        print(f'Days until = {next_date.days_until()}')

print('TEST_7:')
from datetime import date, timedelta

today = date(2023, 4, 23)

for _ in range(7):
    today += timedelta(days=1)
    for weekday in Weekday:
        next_date = NextDate(today, weekday, True)
        print(f'Today = {today} {Weekday(today.weekday()).name}, next {weekday.name} = {next_date.date()}')
        print(f'Days until = {next_date.days_until()}')
