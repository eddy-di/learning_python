class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

point = Point(1, 2, 'red')

for i in point.__dict__.keys():
    k = '{i}'
    print(k)