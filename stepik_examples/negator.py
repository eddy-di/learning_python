from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(object):
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _int_float_neg(object):
        if object < 0:
            return abs(object)
        return object * -1
    
    @neg.register(bool)
    @staticmethod
    def _bool_neg(object):
        if object:
            return False
        else:
            return True
        
not_supported = [[1, 2, 3], (4, 5, 6), {1: 'one'}, {10, 11, 12}, 'Timothy John «Tim» Berners-Lee']

for item in not_supported:
    try:
        Negator.neg(item)
    except TypeError as e:
        print(e)