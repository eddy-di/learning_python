from collections import UserList
from abc import abstractmethod


class Paragraph:
    def __init__(self, length: int, iterable=[]):
        self.length = length
        self.data = iterable

    def add(self, words):
        self.data += words.split()

    @abstractmethod
    def end(self):
        pass

    @staticmethod
    def join_strings(strings_list, max_length):
        result = []
        current_line = []

        for string in strings_list:
            if len(' '.join(current_line + [string])) <= max_length:
                current_line.append(string)
            else:
                result.append(' '.join(current_line))
                current_line = [string]

        result.append(' '.join(current_line))
        return result
    

class LeftParagraph(Paragraph):
    def end(self):
        for i in self.join_strings(self.data, self.length):
            print(f"{i: <{self.length}}")
        self.data = []


class RightParagraph(Paragraph):
    def end(self):
        for i in self.join_strings(self.data, self.length):
            print(f"{i: >{self.length}}")
        self.data = []


# tests

print('TEST_1:')
leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()

# print('TEST_2:')
# rightparagraph = RightParagraph(10)
# 
# rightparagraph.add('death')
# rightparagraph.add('can have me')
# rightparagraph.add('when it earns me')
# rightparagraph.end()

# print('TEST_3:')
# leftparagraph = LeftParagraph(23)
# 
# leftparagraph.add('Multiply noise and joy')
# leftparagraph.add('Sing songs in a good hour')
# leftparagraph.add('Friendship grace and youth')
# leftparagraph.add('Our birthday girls')
# leftparagraph.end()
# 
# leftparagraph.add('Meanwhile the winged child')
# leftparagraph.add('friends greeting you')
# leftparagraph.add('Secretly thinks sometime')
# leftparagraph.add('I will be the birthday boy')
# leftparagraph.end()
# 
print('TEST_4:')
rightparagraph = RightParagraph(28)

rightparagraph.add('I will not regret the roses')
rightparagraph.add('Withered with a light spring')
rightparagraph.add('I love the grapes on the vines')
rightparagraph.add('Ripened in the hands under the mountain')
rightparagraph.end()

rightparagraph.add('The beauty of my green valley')
rightparagraph.add('Golden joy of autumn')
rightparagraph.add('oblong and transparent')
rightparagraph.add('Like the fingers of a young maiden')
rightparagraph.end()