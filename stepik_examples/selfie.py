class Selfie:
    def __init__(self):
        self._state_count = 0
        self._history = {}

    def save_state(self):
        temp = {}
        for k, v in self.__dict__.items():
            temp.setdefault(k, v)
        self._history[self._state_count] = temp
        self._state_count += 1

    def recover_state(self, num: int):
        if num not in self._history:
            new_obj = self.__class__()
            new_obj.__dict__.update(self.__dict__)
        else:
            for k, v in self._history[num].items():
                self.__dict__[k] = v
            new_obj = self.__class__()
            new_obj._state_count = num
            new_obj.__dict__.update(self.__dict__)
        return new_obj

    def n_states(self):
        return self._state_count


# tests

print()
print('TEST_1:')
obj = Selfie()

obj.x = 1
obj.y = 2

print(obj.x)
print(obj.y)

obj.save_state()
obj.x = 0
obj.y = 0

print(obj.x)
print(obj.y)
obj = obj.recover_state(0)
print(obj.x)
print(obj.y)

print()
print('TEST_2:')
obj = Selfie()

print(obj.n_states())
obj.x = 0
obj.save_state()
obj.x = 1
obj.save_state()
obj.x = 2
obj.save_state()
print(obj.n_states())

print()
print('TEST_3:')
from string import ascii_lowercase

obj = Selfie()
for char in ascii_lowercase:
    obj.__dict__[char] = ord(char)

print(*(obj.__dict__[char] for char in ascii_lowercase))
obj.save_state()

for char in ascii_lowercase:
    obj.__dict__[char] = ord(char) + 100

print(*(obj.__dict__[char] for char in ascii_lowercase))
obj = obj.recover_state(0)

print(*(obj.__dict__[char] for char in ascii_lowercase))

print()
print('TEST_4:')
def sum_a_b(a, b):
    return a + b


def sub_a_b(a, b):
    return a - b


def mul_a_d(a, b):
    return a * b


def truediv_a_b(a, b):
    return a / b


obj = Selfie()
obj.sum_a_b = sum_a_b
print(obj.sum_a_b(1, 2))
obj.save_state()

obj.sub_a_b = sub_a_b
print(obj.sub_a_b(1, 2))
obj.save_state()

obj.mul_a_d = mul_a_d
print(obj.mul_a_d(1, 2))
obj.save_state()

obj.truediv_a_b = truediv_a_b
print(obj.truediv_a_b(1, 2))
obj.save_state()

print(obj.n_states())
obj = obj.recover_state(1)

print(obj.n_states())

print()
print('TEST_5:')
obj = Selfie()

obj.x = 1
obj.y = 2

print(obj.x)
print(obj.y)

obj.x = 100
obj.y = 100

obj.save_state()
print(obj.x)
print(obj.y)

obj = obj.recover_state(7)
print(obj.x)
print(obj.y)