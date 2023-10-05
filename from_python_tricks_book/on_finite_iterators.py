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

# This gives us the desired result. Iteration stops after the number of
# repetitions defined in the max_repeats parameter:

# For example:

repeater = BoundedRepeater([1, 2, 3], 3)
for item in repeater:
    print(item)

# Result is
# Hello
# Hello
# Hello

# Without syntactic sugar of for-in loop the example could've been as follows

repeater = BoundedRepeater('Hello', 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)