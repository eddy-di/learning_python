import re

class StrExtension:
    def __init__(self) -> None:
        pass

    @staticmethod
    def remove_vowels(text):
        regex = '[aeiouyAEIOUY]'
        return re.sub(regex, '', text)
    
    @staticmethod
    def leave_alpha(text):
        regex = '[^a-zA-Z]'
        return re.sub(regex, '', text)
    
    @staticmethod
    def replace_all(string, chars, char):
        regex = f'[{chars}]'
        return re.sub(regex, char, string)
    



print(StrExtension.remove_vowels('Success is the ability to go from failure to failure without losing your enthusiasm.'))
print(StrExtension.remove_vowels('Success is the ability to go from failure to failure without losing your enthusiasm.'.upper()))