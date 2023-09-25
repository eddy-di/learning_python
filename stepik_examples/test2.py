t = 'assert_raises_regex'

print(t.count('_'))

def to_upper_camel(text: str) -> str:
    text = text[0].upper() + text[1:]
    while text.count('_') != 0:
        index = text.find('_')
        text = text[:index] + text[index+1].upper() +text[index+2:]
    # while not text.alpha()
    # for i in range(len(text)-1):
        # if text[i] == '_':
            # text = text[:i] + text[i+1].upper() + text[i+2:]
    return text

print(to_upper_camel(t))