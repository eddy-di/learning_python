class CaesarCipher:
    def __init__(self, rotate: int):
        self.rotate = rotate

    def encode(self, text: str):
        result = ""
        for i in range(len(text)):
            char = text[i]
            # get ranges
            if ord(char) in range(65, 91) or ord(char) in range(97, 123):
                # Encrypt uppercase characters
                if (char.isupper()):
                    result += chr((ord(char) + (self.rotate - 65)) % 26 + 65)
                # Encrypt lowercase characters
                else:
                    result += chr((ord(char) + (self.rotate - 97)) % 26 + 97)
            else:
                result += char
        return result
    
    def decode(self, text: str):
        result = ""
        for i in range(len(text)):
            char = text[i]
            # get ranges
            if ord(char) in range(65, 91) or ord(char) in range(97, 123):
                # Encrypt uppercase characters
                if (char.isupper()):
                    result += chr((ord(char) - (self.rotate + 65)) % 26 + 65)
                # Encrypt lowercase characters
                else:
                    result += chr((ord(char) - (self.rotate + 97)) % 26 + 97)
            else:
                result += char
        return result
    





# tests

print()
print('TEST_1:')
cipher = CaesarCipher(10)

print(cipher.encode('Beegeek'))
print(cipher.decode('Gjjljjp'))

print()
print('TEST_2:')
cipher = CaesarCipher(5)

print(cipher.encode('Биgeek123'))
print(cipher.decode('Биljjp123'))

print()
print('TEST_3:')
cipher = CaesarCipher(10)

words = ['leader', 'life', 'central', 'whatever', 'true', 'show', 'year', 'teacher', 'happen', 'might', 'defense',
         'suggest', 'boy', 'trip', 'wish', 'interest', 'star', 'system', 'husband', 'wait', 'young', 'certainly',
         'with', 'wind', 'thought', 'hard', 'today', 'cup', 'where', 'fly', 'agreement', 'human', 'decision', 'along',
         'billion', 'prevent', 'authority', 'those', 'do', 'perform', 'plan', 'allow', 'president', 'do', 'around',
         'seven', 'dog', 'sea', 'use', 'my', 'head', 'whose', 'important', 'top', 'current', 'east', 'page', 'decide',
         'mouth', 'whatever', 'hospital', 'pattern', 'smile', 'probably', 'at', 'evening', 'current', 'local', 'want',
         'foreign', 'catch', 'option', 'meeting', 'course', 'collection', 'street', 'make', 'economic', 'fly', 'return',
         'experience', 'east', 'position', 'foot', 'one', 'mean', 'break', 'me', 'truth', 'management', 'want',
         'option', 'economic', 'response', 'attorney', 'table', 'push', 'travel', 'water', 'help']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

print()
print('TEST_4:')
cipher = CaesarCipher(15)

words = ['EvEr', 'WoUlD', 'CeRtAiN', 'WhIcH', 'WiTh', 'ThErE', 'EnViRoNmEnTaL', 'StRuCtUrE', 'NeWs', 'ThRoW', 'NoTe',
         'If', 'WiN', 'ShOuLdEr', 'NeEd', 'WhErE', 'MeThOd', 'FiRsT', 'CiViL', 'BaSe']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

print()
print('TEST_5:')
cipher = CaesarCipher(15)

words = ['civil😀', 'so😁', 'region☺', 'beat☺', 'artist😍', 'choice🙃', 'include🤭', 'degree😝', 'push🤪', 'side😏', 'size🤥',
         'policy🤨', '🤨🤥😏🤪😝🤭🙃😍☺😁😀']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

print()
print('TEST_6:')
cipher = CaesarCipher(1)
print(cipher.encode('ZzzZzz'))
print(cipher.decode('AaaAaa'))