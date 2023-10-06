import copy

class SequenceZip:
    def __init__(self, *args):
        if len(args) <= 1:
            self.args = args
        self.args = zip(*copy.deepcopy(args))

    def __iter__(self):
        self.copy_iter = copy.deepcopy(self.args)
        return self.copy_iter
    
    def __next__(self):
        self.copy_next = copy.deepcopy(self.args)
        return next(self.copy_next)

    def __len__(self):
        self.copy_len = copy.deepcopy(self.args)
        return len(list(self.copy_len))
        # return min((len(i) for i in self.copy_len), default=0)

    def __getitem__(self, key):
        self.copy_get = copy.deepcopy(self.args)
        for index, element in enumerate(self.copy_get):
            if index == key:
                return element





# print('TEST_1:') 
# sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
# 
# print(list(sequencezip))
# print(tuple(sequencezip))
# 
# print('TEST_2:')
# sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
# 
# print(len(sequencezip))
# print(sequencezip[1])
# print(sequencezip[2])
# 
# print('TEST_3:')
# print(len(SequenceZip([1, 2, 3, 4])))
# print(len(SequenceZip(range(5), [1, 2, 3, 4])))
# print(len(SequenceZip(range(5), [1, 2, 4], 'data')))
# 
# print('TEST_4:')
# x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
# sequencezip = SequenceZip(x, y, z)
# 
# print(sequencezip[2])
# x[-1], z[-1] = z[-1], x[-1]
# print(sequencezip[2])
# 
# print('TEST_5:')
# many_large_sequences = [range(100000) for _ in range(100)]
# sequencezip = SequenceZip(*many_large_sequences)
# print(sequencezip[99999])
# 
# print('TEST_6:')
# sequencezip = SequenceZip()
# print(len(sequencezip))
# print(list(sequencezip))

# print('TEST_7:')
# data1 = [1, 2, 3, 4, 5]
# data2 = 'abcde'

# sequencezip = SequenceZip(data1, data2)
# data1.extend([6, 7, 8, 9, 10])
# data2 += 'fghij'
# 
# print(data1)
# print(data2)
# print(len(sequencezip))
# print(list(sequencezip))