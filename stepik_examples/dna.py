from collections.abc import Sequence


class DNA(Sequence):
    dna_links = {'A': 'T', 
                 'T': 'A', 
                 'G': 'C', 
                 'C': 'G'
                 }

    def __init__(self, chain: str):
        self.chain = chain
        self.data = [(i, self.dna_links[i]) for i in self.chain]

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __str__(self):
        return self.chain
    
    def __contains__(self, value) -> bool:
        flag = False
        for i in self.chain:
            if i == value:
                flag = True
        return flag
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.chain == other.chain
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.chain != other.chain
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.chain + other.chain)
        return NotImplemented
    

    
# tests

print('TEST_1:')
dna = DNA('AGTC')

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[-1])
print(dna[-2])

print('TEST_2:')
dna = DNA('AGT')

print(dna)
print(len(dna))
print('A' in dna)
print('C' in dna)

print('TEST_3:')
dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = dna1 + dna2
dna4 = dna2 + dna1

print(dna3, type(dna3))
print(dna4, type(dna4))

print('TEST_4:')
dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = DNA('TTTAAT')

print(dna1 == dna2)
print(dna2 == dna3)
print(dna1 != dna3)
print(dna2 != dna3)

print('TEST_5:')
dna = DNA('TGAACCTGACCTCGATTTCAAGGG')

print(*dna)
print(*reversed(dna))
print('A' in dna)
print('C' not in dna)

print('TEST_6:')
dna = DNA('ACG')
not_supported = [1, 2.23, [1, 2, 3], {1: 'one'}, {4, 5, 6}, True, False, 'CTA', (7, 8, 9)]

for item in not_supported:
    print(item == dna)

print('TEST_7:')
dnas = ['TAAAACCCCATCGGCTCTGACAATGAAC', 'AGATGTTCCCTCTAATATCTATACGAAT', 'ACGACGCACTGCATACAATACAATAGTG',
        'TCCCAGTCAGGATCGGATTGGTATAATC', 'TACACGCATAGTGCCCAACTCCTACCCG', 'TCACCGCTGAAAACATGTTCTGGAGGGC',
        'CCCAGGATAGACCTATTTGCCGTATCCA', 'ATCGATCGTGCGGGAAATCCTGCCATAT', 'AGACCAACTTATTGGGCACACGCTCCGG',
        'CGCGTCCCCCATATCAACGCGTGAATGC', 'AGTCACGATCAGCTGGACGTAGTGGCAA', 'GTGTAGGGTCAAGGGACACCTGATATCT',
        'AAAAGACGAAAATTGCTAAGTGGCAGTC', 'TGGAGGCCGAGCTCGCGTTGGAAATAGT', 'AAGTCTGCCGAGGCGGGTCGGGAGCGCC',
        'ATTATCCAATCCAGTCACGTATTGAATA', 'ATTGTGAACCTTATACGTTAGTAATACC', 'AGACAATCATGCTATTAGGTATGACGTT',
        'ATCACTGAGGCAGAGACTAGCCGCGCTT', 'TATGGGTGGTATCCTAAGCATTCAATGG']

for base in dnas:
    dna = DNA(base)
    print(*dna)

print('TEST_8:')
dna = DNA('ACG')
print(dna.__eq__(1))
print(dna.__ne__(1.1))
print(dna.__add__([1, 2, 3]))