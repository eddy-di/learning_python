from functools import singledispatchmethod
import datetime
from datetime import date, timedelta

def current_age(birthdate: date, today: date):
    today = date.today()
    in_days = today - birthdate
    res = (in_days / 365.25).days
    return res

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date) -> None:
        self._birth_date = birth_date
        self._age = None
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(datetime.date)
    def _date_type_birth_date(self, birthdate) -> None:
        self.birth_date = birthdate
    
    @__init__.register(str)
    def _iso_date(self, birthdate_iso):
        try:
            self.birth_date = datetime.datetime.fromisoformat(birthdate_iso).date()
        except:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(tuple)
    @__init__.register(list)
    def _tuple_list_date(self, birthdate):
        self.birth_date = datetime.date(*tuple(birthdate))

    @property
    def age(self):
        self.current_date = datetime.date.today()
        self.age_in_days = self.current_date - self.birth_date
        self.age_in_years = (self.age_in_days / 365.25).days
        return self.age_in_years


