class Suppress:
    def __init__(self, *args):
        self.args = args
        self.exception = None

    def __enter__(self):
        return self
    
    def __exit__(self, exc_value, exc_type, traceback):
        if exc_value in self.args:
            self.exception = exc_type
            return True
        return False
    

# tests


print('TEST_1:')
with Suppress(NameError):
    print('Этой переменной не существует -->', variable)
    
print('Завершение программы')

print('TEST_2:')
with Suppress(TypeError, ValueError) as context:
    number = int('я число')

print(context.exception)
print(type(context.exception))

print('TEST_3:')
with Suppress() as context:
    print('All success!')

print(context.exception)

print('TEST_4:')
with Suppress(ValueError) as context:
    try:
        number = list(123)
    except TypeError:
        pass

print(context.exception)

print('TEST_5:')
iterable = iter(range(100))

with Suppress(StopIteration) as context:
    for _ in range(99):
        next(iterable)
    print(next(iterable))
    print(next(iterable))


print(context.exception)
print(type(context.exception))

print('TEST_6:')
d = {'Gvido': 67, 'Gates': 67, 'Zuckerberg': 38}
with Suppress(KeyError) as context:
    print(d['Mask'])


print(context.exception)
print(type(context.exception))

print('TEST_7:')
with Suppress(ValueError) as context:
    try:
        print('Несуществующий метод у словаря –>', {}.new())
    except AttributeError as e:
        print(type(e))

print(context.exception)

print('TEST_8:')
try:
    with Suppress(ValueError) as context:
        number = list(123)
except TypeError:
    pass

print(context.exception)