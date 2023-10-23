
        

iterable = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
obj = 4
del_index = find(obj, iterable)

while True:
    if iterable[del_index] == obj:
        iterable.pop(del_index)
    else:
        break


print(iterable)



