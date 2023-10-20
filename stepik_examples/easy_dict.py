from typing import Any


class EasyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, __name: str) -> Any:
        return super().__getitem__(__name)

# tests

print('TEST_1:')
easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

print(easydict['name'])
print(dir(easydict))
print(easydict.city)

print('TEST_2:')
easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

easydict['city'] = 'Dubai'
easydict['age'] = 30
print(easydict.city)
print(easydict.age)

print('TEST_3:')
easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})

easydict.age = 21
print(easydict)

print('TEST_4:')
d = {'Савелий': 33, 'Осип': 50, 'Измаил': 20, 'Евсей': 34, 'Ермил': 35, 'Родион': 45, 'Назар': 44, 'Арефий': 47,
     'Ипатий': 44, 'Лонгин': 26, 'Адам': 43, 'Изяслав': 45, 'Вячеслав': 20, 'Леонид': 30, 'Адриан': 38, 'Гордей': 43,
     'Сидор': 29, 'Ефим': 23, 'Лавр': 36, 'Тарас': 33, 'Платон': 41, 'Наркис': 29, 'Карп': 21, 'Юлий': 44,
     'Сигизмунд': 23, 'Будимир': 22, 'Галактион': 24, 'Никон': 22, 'Олимпий': 33, 'Геннадий': 21, 'Тимур': 35,
     'Арсений': 44, 'Всеволод': 39, 'Ратмир': 31, 'Ипполит': 21, 'Касьян': 46, 'Венедикт': 32, 'Валентин': 44,
     'Эмиль': 22, 'Елизар': 38, 'Борис': 34, 'Кирилл': 33, 'Антип': 35, 'Влас': 29, 'Мстислав': 46, 'Амос': 21,
     'Мартьян': 22, 'Наталья': 45, 'Регина': 43, 'Ольга': 47, 'Василиса': 22, 'Глафира': 48, 'Елена': 45,
     'Алевтина': 21, 'Екатерина': 28, 'Нина': 32, 'Виктория': 22, 'Агафья': 30, 'Анна': 20, 'Жанна': 37, 'София': 28,
     'Светлана': 24, 'Юлия': 46, 'Эмилия': 32, 'Надежда': 45, 'Милица': 27, 'Антонина': 31, 'Синклитикия': 38,
     'Татьяна': 27, 'Вера': 26, 'Анастасия': 49, 'Александра': 42, 'Евдокия': 28, 'Клавдия': 25, 'Ксения': 42,
     'Евгения': 20, 'Тамара': 47, 'Галина': 23, 'Нонна': 47, 'Фаина': 22, 'Ангелина': 43, 'Марина': 21, 'Лора': 33}

easydict = EasyDict(d)
easydict['Боян'] = 30

print(easydict.Боян)
print(easydict.Кирилл)
print(easydict.Антонина)
print(easydict.Назар)
print(easydict.Галина)

print(easydict['Ипполит'])
print(easydict['Мстислав'])
print(easydict['Сигизмунд'])
print(easydict['Фаина'])
print(easydict['Жанна'])