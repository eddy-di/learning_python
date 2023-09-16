lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_"\''

text_input = input()

def my_split():
	res = []
	word = ''
	for i in range(len(text_input)):
		if i == (len(text_input) - 1) and (text_input[i] in lower_case or text_input[i] in upper_case) and text_input[i] not in punctuation:
			word += text_input[i]
			res.append(word)    
		elif text_input[i] in lower_case or text_input[i] in upper_case:
			word += text_input[i]
		elif text_input[i] in ' ':
			res.append(word)
			word = ''
		elif i == len(text_input) - 1:
			res.append(word)
		elif text_input[i] in punctuation:
			pass
	return res

def encrypt_eng():
	list = my_split()
	res = []
	for word in range(len(list)):
		s = list[word]

		result = ""
		for i in range(len(s)):
			char = s[i]
			# Encrypt uppercase characters
			if (char.isupper()):
				result += chr((ord(char) + (len(s) - 65)) % 26 + 65)

			# Encrypt lowercase characters
			else:
				result += chr((ord(char) + (len(s) - 97)) % 26 + 97)
		
		res.append(result)
	return res

def my_join():
    text = text_input.split()

    res = encrypt_eng()

    text = ' '.join(text)
    res = ' '.join(res)

    i1 = 0
    i2 = 0

    while i1 < len(text) and i2 < len(res) or i1 == len(text) and i2 > len(res):

        if text[i1].isalpha() and res[i2].isalpha():
            i1 += 1
            i2 += 1
        elif 33 <= ord(text[i1]) <= 47 and res[i2].isspace():
            res = res[:i2] + text[i1] + res[i2:]
            i1 += 1
            i2 += 1
        elif 33 <= ord(text[i1]) <= 47 and res[i2].isalpha():
            res = res[:i2] + text[i1] + res[i2:]
            i1 += 1
            i2 += 1
        else:
            i1 += 1
            i2 += 1
            pass

    if len(text) != len(res):
        res = res[:] + text[-1] 

    return res



print(my_join())
