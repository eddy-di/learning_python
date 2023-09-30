class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        # self.attrs_num = 0
        # self.attrs_num += len(self.__dict__)

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value

    def __getattr__(self, attr):
        if attr == 'attrs_num':
            return len(self.__dict__) + 1



music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)