class LoopTracker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.behind_accesses = -1
        self.original = [i for i in iterable]
        self._accesses = 0
        self.empty_accesses = 0

    def __iter__(self):
        return self.iterable
    
    @property
    def accesses(self):
        return self._accesses
    
    def __next__(self):
        self.item = next(self.iterable, Ellipsis)
        if self.item == Ellipsis or self.item == None:
            self.empty_accesses += 1
            raise StopIteration
        else:
            self._accesses += 1
            self.behind_accesses += 1
            return self.item
        
        
    @property
    def first(self):
        if self.original == []:
            raise AttributeError("Исходный итерируемый объект пуст")
        return self.original[0]
    
    @property
    def last(self):
        if self.original == [] or self.behind_accesses == -1:
            raise AttributeError("Последнего элемента нет")
        return self.original[self.accesses - 1]

    def is_empty(self):
        if 0 <= self.accesses <= len(self.original) - 1:
            return False
        return True
    

# TEST_2:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)

# TEST_3:
loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

# TEST_4:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

# TEST_5:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.empty_accesses)
next(loop_tracker)
next(loop_tracker)

for _ in range(5):
    try:
        next(loop_tracker)
    except StopIteration:
        pass
        
print(loop_tracker.empty_accesses)

# TEST_6:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())

# TEST_7:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.first)
print(next(loop_tracker))

# TEST_8:
loop_tracker = LoopTracker([])

try:
    print(loop_tracker.first)
except AttributeError as e:
    print(e)

# TEST_9:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)
print(next(loop_tracker))
print(loop_tracker.last)

# TEST_10:
loop_tracker = LoopTracker([1, 2, 3])

try:
    print(loop_tracker.last)
except AttributeError as e:
    print(e)

# TEST_11:
loop_tracker = LoopTracker(range(1_000))

for _ in range(100_000):
    next(loop_tracker, None)

print(loop_tracker.accesses)
print(loop_tracker.empty_accesses)

# TEST_12:
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())