# In Python 3, the method that retrieves the next value from an
# iterator is called __next__.
# In Python 2, the same method is called next (no underscores).

class InfiniteRepeater(object):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value
    
    # Python 2 compatibility
    def next(self):
        return self.__next__()
