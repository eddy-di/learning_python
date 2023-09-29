class Queue:
    def __init__(self, *args):
        self.args = list(args)

    def add(self, *args_add):
        if isinstance(args_add, tuple):
            return self.args.extend(list(args_add))
        return NotImplemented
    
    def pop(self):
        if len(self.args) != 0:
            return self.args.pop(0)
        return None
    
    def __str__(self):
        return f'{" -> ".join(map(str, self.args))}'
    
    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            if len(other.args) == len(self.args):
                return all([self.args[i] == other.args[i] for i in range(len(self.args))])
            else:
                return False
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(*tuple(self.args + other.args))
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.args += other.args
            return self
        return NotImplemented
        
    def __rshift__(self, n):
        if isinstance(n, int):
            if n < len(self.args):
                return self.__class__(*self.args[n:])
            elif n >= len(self.args):
                return self.__class__(*self.args[0:0])
        return NotImplemented
        
queue = Queue(1, 2, 3)
print(queue.__add__([]))
print(queue.__iadd__('bee'))
print(queue.__rshift__('geek'))