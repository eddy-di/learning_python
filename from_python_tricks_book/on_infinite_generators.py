# rewriting infinite iterator into a generator
def repeater(value):
    while True:
        yield value


# counter = 0 # counter is necessary to not make it infinite
# for x in repeater('Hi'):
    # print(x)
    # counter += 1
    # if counter > 100:
        # break

# Now, how do these generators work? They look like normal functions,
# but their behavior is quite different. For starters, calling a generator
# function doesn’t even run the function. It merely creates and returns
# a generator object:

# repeater('Hey')
# print(repeater('Hey')) # gives <generator object repeater at 0x7f730de662c0>

# The code in the generator function only executes when next() is
# called on the generator object:

generator_obj = repeater('Hey')
print(next(generator_obj)) # returns given value -> 'Hey'

# If you read the code of the repeater function again, it looks like the
# yield keyword in there somehow stops this generator function in mid-
# execution and then resumes it at a later point in time:

# def repeater(value):
    # while True:
        # yield value

# And that’s quite a fitting mental model for what happens here.
# when you end code with return - it gives a result of a function permanently, meaning it executes its function and that's it finito
# when you end code with yield - it gives a result of a fucntion temporarily, meaning one by one without completely finishing process
# execution of yield can be resumed by calling next() on the generator