import re

class CaseHelper:
    @staticmethod
    def is_snake(text: str) -> bool:
        regex = '^[a-z]*_*[a-z]*$'
        res = re.match(regex, text)
        return True if res else False
    
    @staticmethod
    def is_upper_camel(text: str) -> bool:
            regex = '[A-Z][a-z0-9]*[A-Za-z0-9]*'
            res = re.match(regex, text)
            return True if res else False
    
    @staticmethod
    def to_snake(text: str) -> str:
        text = text[0].lower() + text[1:]
        for i in range(len(text)-1):
            if text[i].isupper() and i != 0:
                text = text[:i] + '_' + text[i].lower() + text[i+1:]
        return text
    
    @staticmethod
    def to_upper_camel(text: str) -> str:
        text = text[0].upper() + text[1:]
        while text.count('_') != 0:
            index = text.find('_')
            text = text[:index] + text[index+1].upper() +text[index+2:]
        return text


cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']

for case in cases:
    print(CaseHelper.to_upper_camel(case))
