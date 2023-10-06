class SequenceZip:
    def __init__(self, *args):
        self.sequences = (iter(seq) for seq in args)

    def __len__(self):
        return min(len(seq) for seq in self.sequences)

    def __iter__(self):
        return self.generator()

    def generator(self):
        min_length = len(self)
        for i in range(min_length):
            yield tuple(next(seq) for seq in self.sequences)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        return tuple(seq[index] for seq in self.sequences)
    

print('TEST_1:') 
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))

print('TEST_2:')
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])

print('TEST_3:')
print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], 'data')))

print('TEST_4:')
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])

print('TEST_5:')
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])

print('TEST_6:')
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))
# 
print('TEST_7:')
data1 = [1, 2, 3, 4, 5]
data2 = 'abcde'

sequencezip = SequenceZip(data1, data2)
data1.extend([6, 7, 8, 9, 10])
data2 += 'fghij'

print(data1)
print(data2)
print(len(sequencezip))
print(list(sequencezip))