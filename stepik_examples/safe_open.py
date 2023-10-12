from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    file_obj = None
    exception = None
    try:
        file_obj = open(filename, mode)
        yield file_obj, None
    except Exception as e:
        yield None, e
    finally:
        if file_obj is not None:
            file_obj.close()




# tests

print('TEST_1:')
with open('Ellies_jokes.txt', 'w') as file:
    file.write('Знаешь, кто не прав? Лев\n')
    file.write('Что треугольник сказал кругу? Катись отсюда')
    
with safe_open('Ellies_jokes.txt') as file:
    file, error = file
    print(error)
    print(file.read())

print('TEST_2:')
with safe_open('Ellies_jokes_2.txt') as file:
    file, error = file
    print(file)
    print(error)

print('TEST_3:')
text = '''Кричит ворона в небе: – Кар-р!
В лесу пожар-р, в лесу пожар-р!
А было просто очень:
В нём поселилась осень.'''

with open('file.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with safe_open('file.txt', 'r') as file:
    file, error = file
    print(file.read())
    print(error)

print('TEST_4:')
with open('file.txt', 'w') as file:
    file.write('Как говорится, земля круглая, за углом встретимся.')

with safe_open('file.txt', 'rb') as file:
    f, error = file
    print(f)
    print(error)

print('TEST_5:')
files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt', 'file7.txt', 'file8.txt',
         'file9.txt', 'file10.txt', 'file11.txt', 'file12.txt', 'file13.txt', 'file14.txt', 'file15.txt', 'file16.txt',
         'file17.txt', 'file18.txt', 'file19.txt', 'file20.txt']

for f in files:
    with safe_open(f) as file:
        file, error = file
        print(file)
        print(error)

print('TEST_6:')
with open('Couplet.txt', 'w') as file:
    file.write('Так уносились мы мечтой\n')
    file.write('К началу жизни молодой')

with safe_open('Couplet.txt') as file:
    file, error = file
    print(error)
    print(file.read())

    print(file.closed)

print(file.closed)