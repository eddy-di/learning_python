class ReversedSequence:
    def __init__(self, iterable):
        self.iterable = iterable
    
    def __len__(self):
        return len(self.iterable)
    
    def check_key(self, key):
        if not isinstance(key, int):
            raise TypeError
        if key < 0 or key >= len(self.iterable):
            raise IndexError
        return key
    
    def __getitem__(self, key):
        key = self.check_key(key)
        return self.iterable[~key]
    
    def __setitem__(self, key, value):
        key = self.check_key(key)
        self.iterable[key] = value

    def __contains__(self, item):
        return item in self.iterable
    

reversed_list = ReversedSequence(['Gvido', 'Elon', 'Gates', 'Jobs', 'Zuckerberg'])

print(*reversed(reversed_list))