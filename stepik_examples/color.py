class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode
        self._r = self._hexcode[0:2]
        self._g = self._hexcode[2:4]
        self._b = self._hexcode[4:6]

    @property
    def hexcode(self):
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, new_hexcode):
        self._hexcode = new_hexcode
        self._r = self._hexcode[0:2]
        self._g = self._hexcode[2:4]
        self._b = self._hexcode[4:6]

    @property
    def r(self):
        return int(self._r, 16)

    @property
    def g(self):
        return int(self._g, 16)
    
    @property
    def b(self):
        return int(self._b, 16)

hexcodes = ['FC5A5E', '13AABE', '851149', 'AAAAAA', 'FFFFFF', 'B6A1D8', 'ABCDEF', 'FEDCBA', '123456', '999999']
count = 1
for hc in hexcodes:
    color = Color(hc)
    print(f'Цвет № {count}')
    print(color.hexcode)
    print(color.r, color.g, color.b, sep='\n')
    print()
    count += 1