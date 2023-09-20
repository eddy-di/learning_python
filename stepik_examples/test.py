iterable = iter('Beegeek')

temp = []
delimiter = '+'

for index, value in enumerate(list(iterable)):
    if index != len(iterable)-1:
        temp.append(value)
        temp.append(delimiter)
    else:
        temp.append(value)

print(*iterable)
print(*temp)