class SkipIterator:
    def __init__(self, iterator, num):
        self.iterator = [i for i in iterator]
        self.num = num
        self.res = []
        self.start = -1
        for i in range(0, len(self.iterator), 1+self.num):
            self.res.append(self.iterator[i])

    def __iter__(self):
        for i in range(0, len(self.iterator), 1+self.num):
            self.res.append(self.iterator[i])
            yield self.iterator[i]
    
    def __next__(self):
        self.start = self.start + 1
        if self.start > len(self.res):
            raise StopIteration
        return self.res[self.start]




skipiterator = SkipIterator(range(1000), 7)

for _ in range(25):
    next(skipiterator)

print(next(skipiterator))
print(next(skipiterator))
print(next(skipiterator))
