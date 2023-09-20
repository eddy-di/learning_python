sequence = [3, 1, 4, 2]

def inversions(sequence):
    counter = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if i < j and sequence[i]>sequence[j]:
                counter += 1
    return counter

print(inversions(sequence))