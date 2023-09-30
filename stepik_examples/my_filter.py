class Filter:
    def __init__(self, func) -> None:
        self.predicate = func

    def __call__(self, iterable):
        if self.predicate == None:
            self.predicate = bool
        return list(filter(self.predicate, iterable))


empty_elements = Filter(lambda x: not x)

sequence = [(1, 2, 3), [], set(), 'Beegeek', {}, {1: '12'}, False, True, '', [2023, 4]]
print(empty_elements(sequence))

