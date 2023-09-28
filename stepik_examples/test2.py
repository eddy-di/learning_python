m = []
counter = 1
for row in range(4):
    temp = []
    for col in range(2):
        temp.append(counter)
        counter += 1
    m.append(temp)
    temp = []


transpose = [[m[j][i] for j in range(4)] for i in range(2)]

for r in m:
    print(*r)
print()
for r in transpose:
    print(*r)
