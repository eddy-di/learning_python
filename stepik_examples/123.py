from datetime import date, timedelta


today = date.today()

res = today + timedelta(days=5)
print(type(res))

days_left = res - today

print(days_left.days)