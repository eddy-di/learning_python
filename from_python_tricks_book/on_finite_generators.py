# an example of a generator that is finite, more precisely three times
def repeat_three_times(value):
    yield value
    yield value
    yield value

for x in repeat_three_times('Hey there'):
    print(x)

# Result is:
# Hey there
# Hey there
# Hey there

# Previously on iterators there was a class for limited number of iterations
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_repeats: #condition that stops iteration
            raise StopIteration 
        self.count += 1
        return self.value

# There's version of it's generator without syntactic for-in sugar
# def bounded_repeater(value, max_repeats):
    # count = 0
    # while True:
        # if count >= max_repeats:
            # return
        # count += 1
        # yield value

# try the generator out
# for x in bounded_repeater('Hi', 4):
    # print(x)

# result:
# Hi
# Hi
# Hi
# Hi

def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value