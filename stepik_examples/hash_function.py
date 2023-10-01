def hash_function(obj):
    if type(obj) != str:
        obj = str(obj)
    # 1
    temp1 = 0
    pos_count = 0
    neg_count = -1
    if len(obj) % 2 == 0:
        while pos_count != len(obj) // 2:
            res = ord(obj[pos_count]) * ord(obj[neg_count])
            pos_count += 1
            neg_count -= 1
            temp1 += res
    else:
        temp1 += ord(obj[len(obj)//2])
        t = obj[len(obj)//2]
        obj = obj[:(len(obj)//2)]+obj[len(obj)//2+1:]
        while pos_count != (len(obj) // 2):
            res = ord(obj[pos_count]) * ord(obj[neg_count])
            pos_count += 1
            neg_count -= 1
            temp1 += res
        obj = obj[:(len(obj)//2)] + t + obj[len(obj)//2:]
    # 2
    temp2 = 0
    for i in range(len(obj)):
        if i % 2 == 0:
            temp2 += ord(obj[i]) * (i+1)
        else:
            temp2 -= ord(obj[i]) * (i+1)
    # 3
    total_hash = (temp1 * temp2) % 123456791
    return total_hash

print(hash_function([1, 2, 3, 'python']))