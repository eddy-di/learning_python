s = '-p'

p = 'p'

for c in s:
    print(ord(c))


print(ord('p'))
res = list(map(lambda x: True if 48 <= ord(x) <= 57 or ord(x[0]) == 45 else False, s))

print(res)