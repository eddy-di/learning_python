from random import shuffle

class RandomLooper:
    def __init__(self, *args):
        self.args = args
        self.flattened = [j for i in args for j in i]
        shuffle(self.flattened)
        self.iterable = iter(self.flattened)

    def __iter__(self):
        return self.iterable
    
    def __next__(self):
        return next(self.iterable)


randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

answer = [next(randomlooper) for _ in range(4)]
print(answer)
