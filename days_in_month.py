from datetime import datetime, timedelta

# Указываем месяц и год
year = 2012
month = 3

# Создаем начальную дату (первый день месяца)
start_date = datetime(year, month, 1)

# Определяем последний день месяца
if month == 12:
    end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
else:
    end_date = datetime(year, month + 1, 1) - timedelta(days=1)

# Создаем счетчики для каждого дня недели
day_counts = [0, 0, 0, 0, 0, 0, 0]  # Пн, Вт, Ср, Чт, Пт, Сб, Вс

res = None

# Создаем цикл для перебора дат в месяце
current_date = start_date
while current_date <= end_date:
    day_of_week = current_date.weekday()  # Номер дня недели (0 - понедельник, 1 - вторник, и так далее)
    day_counts[day_of_week] += 1  # Увеличиваем счетчик для соответствующего дня недели
    if day_counts[3] == 4:
        res = current_date
    else:
        current_date += timedelta(days=1)  # Переходим к следующей дате


formated_date = res.strftime("%d.%m.%Y")

print(formated_date)

# Выводим результаты
# days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# for i, day in enumerate(days):
#     if i == 3:
#         print(f"{day}: {day_counts[i]}")