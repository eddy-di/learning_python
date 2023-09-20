from datetime import datetime, timedelta

# Указываем начальную и конечную даты
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Создаем счетчики для каждого дня недели
day_counts = [0, 0, 0, 0, 0, 0, 0]  # Пн, Вт, Ср, Чт, Пт, Сб, Вс

# Создаем цикл для перебора дат в диапазоне
current_date = start_date
while current_date <= end_date:
    day_of_week = current_date.weekday()  # Номер дня недели (0 - понедельник, 1 - вторник, и так далее)
    day_counts[day_of_week] += 1  # Увеличиваем счетчик для соответствующего дня недели
    current_date += timedelta(days=1)  # Переходим к следующей дате

# Выводим результаты
days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
for i, day in enumerate(days):
    print(f"{day}: {day_counts[i]}")