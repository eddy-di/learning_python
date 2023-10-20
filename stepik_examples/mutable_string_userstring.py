from collections import UserString


class MutableString(UserString):
    def upper(self):
        self.data = self.data.upper()
        return self.data
    
    def lower(self):
        self.data = self.data.lower()
        return self.data
    
    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))
        return self.data
    
    def __setitem__(self, key, item):
        self.data = self.data[:key] + item + self.data[key+1:]

    def __delitem__(self, key):
        self.data = self.data[:key] + self.data[key+1:]

    

# tests

print('TEST_1:')
mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)

print('TEST_2:')
mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)

print('TEST_3:')
words = ['improve', 'north', 'now', 'there', 'outside', 'set', 'into', 'time', 'campaign', 'onto', 'change', 'source',
         'use', 'huge', 'specific', 'consumer', 'speak', 'card', 'century', 'late', 'focus', 'money', 'successful',
         'myself', 'available', 'rise', 'no', 'charge', 'hit', 'friend', 'cost', 'billion', 'financial', 'model',
         'decade', 'whole', 'space', 'service', 'agreement', 'home', 'represent', 'away', 'describe', 'plan', 'drop',
         'dream', 'leg', 'mouth', 'interesting', 'provide', 'indeed', 'thing', 'practice', 'miss', 'bring', 'important',
         'court', 'talk', 'true', 'conference', 'tell', 'issue', 'identify', 'hand', 'appear', 'stuff', 'run',
         'present', 'good', 'region', 'detail', 'recognize', 'international', 'behavior', 'attack', 'politics', 'great',
         'baby', 'measure', 'whether', 'yard', 'with', 'pressure', 'role', 'eight', 'man', 'she', 'four', 'them',
         'adult', 'clear', 'marriage', 'meeting', 'notice']

for word in words:
    mutablestring = MutableString(word)
    print(mutablestring, end=' ')

    mutablestring.upper()
    print(mutablestring, end=' ')

    mutablestring.sort(key=lambda char: -ord(char), reverse=True)
    print(mutablestring)

print('TEST_4:')
text = '''Spelling: my last name is two words, and I'd like to keep it that way, the spelling on some of my credit
cards notwithstanding. Dutch spelling rules dictate that when used in combination with my first name, "van" is not
capitalized: "Guido van Rossum". But when my last name is used alone to refer to me, it is capitalized, for example:
"As usual, Van Rossum was right."'''

mutablestring = MutableString(text)

mutablestring[208] = 'V'
mutablestring[209] = 'A'
mutablestring[210] = 'N'
print(mutablestring)

print('TEST_5:')
text = 'Beautiful is better than ugly.'

mutablestring = MutableString(text)

del mutablestring[9]
print(mutablestring)

del mutablestring[-6]
print(mutablestring)