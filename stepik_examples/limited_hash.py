def limited_hash(left: int, right: int, hash_function=hash):
    nums = [i for i in range(left, right + 1)]
    def func(x):
        r = hash_function(x)
        if r in range(left, right + 1):
            return r
        if r not in range(left, right + 1) and r > right:
            while r not in range(left, right + 1):
                r -= len(nums)
            return r
        if r not in range(left, right + 1) and r < left:
            while r not in range(left, right + 1):
                r += len(nums)
            return r
    return func

        # if r > right:
            # computing = (r % (right)) % (len(nums))
            # return left + (computing - 1 if computing > 0 else right - left)
        # elif r < left:
            # computing = (r + (right // left)) % len(nums)
            # if computing in range(left, right + 1):
                # return computing
            # return left + (computing + 1 if computing < (right - left) else 0)

def hash_function(obj):
    return sum(index * ord(character) for index, character in enumerate(str(obj), start=1))


hash_function = limited_hash(10, 15, hash_function)

array = [1366, -5502567186.7395, 'zZQyrjYzdgcabTZPATPl', False, {'монета': -671699723096.267, 'лететь': 5151},
         (False, True, 897, -844416.51017117, 1101),
         [True, 171664.794743347, True, False, 'UypAaBSjBWYWBYbmRTdN', 4044844490314.56]]

for item in array:
    print(hash_function(item))