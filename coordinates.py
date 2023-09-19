import sys

coordinates = [coordinate.strip().split(', ') for coordinate in sys.stdin]

working = []
for lt in coordinates:
    res = float(lt[0][1:]), float(lt[1][:-1])
    working.append(tuple(res))

for el in working:
    if -90 <= el[0] <= 90 and -180 <= el[1] <= 180:
        print(True)
    else:
        print(False)

