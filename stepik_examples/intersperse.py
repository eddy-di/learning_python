
def intersperse(iterable, delimiter):
    if iterable != False:
        iter_t = list(iterable)
    else:
        return 
    temp_iter = iter_t.copy()
    last_element = None
    for el in temp_iter:
        last_element = el
    res = []
    for i in iter_t:
        if i != last_element:
            res.append(i)
            res.append(delimiter)
        else:
            res.append(i)
    return res


            

iterable1 = []

# print(*iterable1)
print(*intersperse(iterable1, '+'))
