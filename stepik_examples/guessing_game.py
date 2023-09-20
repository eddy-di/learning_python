import random

num = random.randint(1, 101)

print("Добро пожаловать в числовую угадайку\n")

def again():
    while True:
        again = input('Ещё раз? (д = да, н = нет): ')
        if again.lower() == 'д':
            num = random.randint(1, 101)
            return guess()
        else:
            break

def is_valid(arg):
    if arg.isdigit() and 1 <= int(arg) <= 100:
        return True  # checks if its numerical and if its in acceptable range

def good_input(): # looping over to make an input a good one part of foolproofness
    while True: 
        guess = input('Введите целое число от 1 до 100\n')
        if is_valid(guess):
            return int(guess)
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")

def guess():
    counter = 0
    while True:
        arg = good_input()
        if arg > num:
            counter += 1
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif arg < num:
            counter += 1
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif arg == num:
            counter += 1
            print("Вы угадали, поздравляем!")
            print(f'Всего попыток было сделано {counter}')
            counter = 0
            return again()
        else:
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break

guess()

