class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.close()
        except Exception:
            raise ValueError('Файл закрыт или недоступен для записи')
    
    def write(self, text):
        try: 
            if self.writable:
                self.file1.write(text)
                self.file2.write(text)
        except Exception:
            raise ValueError('Файл закрыт или недоступен для записи')
        
    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self) -> bool:
        if (self.file1.mode.startswith('w') and not self.file1.closed) and (self.file2.mode.startswith('w') and not self.file2.closed):
            return True
        return False
    
    def closed(self):
        if self.to_close == False:
            return False
        return self.file1.closed and self.file2.closed
    

# tests




print('TEST_1:')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    combined.write('You shall seal the blinding light that plagues their dreams\n')
    combined.write('You are the Vessel\n')
    combined.write('You are the Hollow Knight')

print(f1.closed, f2.closed)

with open('file1.txt') as file1, open('file2.txt') as file2:
    print(file1.read())
    print(file2.read())

print('TEST_2:')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())
    
f1 = open('file1.txt')
f2 = open('file2.txt')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

print('TEST_3:')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.closed())
    f1.close()
    print(combined.closed())
    f2.close()
    print(combined.closed())

print('TEST_4:')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=False) as combined:
    print(f1.closed, f2.closed)
    combined.close()
    print(f1.closed, f2.closed)

print('TEST_5:')
f1 = open('file1.txt', mode='r')
f2 = open('file2.txt', mode='w')

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)

print('TEST_6:')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)


print('TEST_7:')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

print('TEST_8:')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    pass

print(combined.closed())

print('TEST_9:')
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2) as combined:
    pass

print(combined.closed())