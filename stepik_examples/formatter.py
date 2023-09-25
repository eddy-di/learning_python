from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(object):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @format.register(int)
    @staticmethod
    def _int_format(object):
        print('Целое число:', object)
    
    @format.register(float)
    @staticmethod
    def _float_format(object):
        print('Вещественное число:', object)
    
    @format.register(tuple)
    @staticmethod
    def _tuple_format(object):
        str_objects = (str(i) for i in object)
        print('Элементы кортежа:', ', '.join(str_objects))

    @format.register(list)
    @staticmethod
    def _list_format(object):
        str_objects = (str(i) for i in object)
        print('Элементы списка:', ', '.join(str_objects))

    @format.register(dict)
    @staticmethod
    def _dict_format(object):
        str_objects = (str(i) for i in object.items())
        print('Пары словаря:', ', '.join(str_objects))

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})