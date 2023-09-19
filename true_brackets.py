s = '((()))' # input()

while len(s) != 0:
    index = s.find('()')
    s = s.replace(s[index:index+2], '')
    if len(s) == 0:
        print(True)
    else:
        print(False)
        break