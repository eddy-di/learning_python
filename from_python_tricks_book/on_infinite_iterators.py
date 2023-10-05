# first option with two seperate classes handling different types of functionalities

class Repeater1:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)
    
class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    
    def __next__(self):
        return self.source.value
    
repeater = Repeater1('Hello')

counter = 0
for item in repeater:
    print(item)
    counter += 1
    if counter > 100:
        break

# What exactly happens when the for-in loop is called, afterwards an example of the way how it works under the hood
# # # repeater = Repeater('Hello')
# # # iterator = repeater.__iter__()
# # # while True: # this makes an infinite loop
# #     # item = iterator.__next__()
# #     # print(item)
# As you can see, the for-in was just syntactic sugar for a simple while loop:
# It first prepared the repeater object for iteration by calling its __iter__ method. This returned the actual iterator object.
# After that, the loop repeatedly called the iterator object’s __next__ method to retrieve values from it.

# second option where __iter__ and __next__ is present in one single class

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value
    
