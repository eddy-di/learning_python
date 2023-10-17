class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date):
        print(date.strftime('%d.%m.%Y'))
        return super().rain()
    
    def snow(self, date):
        print(date.strftime('%d.%m.%Y'))
        return super().snow()
    
    def low_temperature(self, date):
        print(date.strftime('%d.%m.%Y'))
        return super().low_temperature()
    

# tests

print('TEST_1:')
print(issubclass(WeatherWarningWithDate, WeatherWarning))

print('TEST_2:')
weatherwarning = WeatherWarning()

weatherwarning.rain()
weatherwarning.snow()
weatherwarning.low_temperature()

print('TEST_3:')
from datetime import date

weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)

print('TEST_4:')
from datetime import date

weatherwarning = WeatherWarningWithDate()
dates = [date(2004, 6, 29), date(2012, 2, 1), date(1973, 2, 1), date(2020, 7, 8), date(2003, 2, 19), date(2022, 12, 25),
         date(2012, 8, 24), date(1977, 8, 5), date(2017, 5, 26), date(1976, 1, 8), date(2017, 11, 13), date(1989, 3, 4),
         date(1971, 12, 9), date(2011, 11, 13), date(1970, 6, 29), date(1983, 5, 11), date(1984, 8, 9),
         date(1999, 6, 15), date(2011, 3, 14), date(1980, 5, 26)]

for dt in dates:
    weatherwarning.rain(dt)
    weatherwarning.snow(dt)
    weatherwarning.low_temperature(dt)