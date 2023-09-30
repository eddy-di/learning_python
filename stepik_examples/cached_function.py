class CachedFunction:
    def __init__(self, func):
        self.apply = func
        self.cache = {}
    
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.apply(*args)
        return self.cache[args]

    

@CachedFunction
def tribonacci(n):
    if n in (1, 2, 3):
        return 1
    return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)


print(tribonacci(200))
print(len(tribonacci.cache))