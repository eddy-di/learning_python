class HourClock:
    def __init__(self, hours: int):
        if hours in range(1, 13):
            self._hours = hours
        else:
            raise ValueError('Некорректное время')
        
    def get_hour(self):
        return self._hours
    
    def set_hour(self, new_hour: int):
        if new_hour in range(1, 13):
            self._hours = new_hour
        else:
            raise ValueError('Некорректное время')
        
    hours = property(fget=get_hour, fset=set_hour)


time = HourClock(1)
print(hasattr(HourClock, 'hours'))
