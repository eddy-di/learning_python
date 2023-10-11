class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, *args, **kwargs):
        print(f'До встречи, {self.name}!')


# tests

print('TEST_1:')
with Greeter('Кейв'):
    print('...')

print('TEST_2:')
with Greeter('Кейв') as greeter:
    print(greeter.name)

print('TEST_3:')
with Greeter('Матильда') as greeter:
    pass

print('TEST_4:')
with Greeter('Михаил Г.') as greeter:
    print(
        '\nКак бессонница в час ночной\n'
        'Меняет, нелюдимая, облик твой,\n'
        'Чьих невольница ты идей?\n'
        'Зачем тебе охотиться на людей?\n'
    )

print('TEST_5:')
with Greeter('Gvido') as greeter:
    try:
        print(greeter.age)
    except AttributeError as e:
        print(f'Атрибут "{e.name}" отсутствует')