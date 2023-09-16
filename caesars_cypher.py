
def encrypt_eng(text,s):
	result = ""

	for i in range(len(text)):
		char = text[i]
		
		# ignore punctuation
		if 32 <= ord(char) <= 47:
			result += char
	    
		# Encrypt uppercase characters
		elif (char.isupper()):
			result += chr((ord(char) + (s - 65)) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + (s - 97)) % 26 + 97)

	return result

def decrypt_eng(text,s):
	result = ""

	for i in range(len(text)):
		char = text[i]
		
		# ignore punctuation
		if 32 <= ord(char) <= 47:
			result += char
	    
		# Encrypt uppercase characters
		elif (char.isupper()):
			result += chr((ord(char) - (s + 65)) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) - (s + 97)) % 26 + 97)

	return result

def encrypt_rus(text,s):
	result = ""

	for i in range(len(text)):
		char = text[i]
		
		# Игнорирование пунктуационных символов
		if 32 <= ord(char) <= 47:
			result += char
	    
		# Шифрование верхнего регистра
		elif (char.isupper()):
			result += chr((ord(char) + (s - 1040)) % 32 + 1040)

		# Шифрование нижнего регистра
		else:
			result += chr((ord(char) + (s - 1072)) % 32 + 1072)

	return result

def decrypt_rus(text,s):
	result = ""

	for i in range(len(text)):
		char = text[i]
		
		# Игнорирование пунктуационных символов
		if 32 <= ord(char) <= 47:
			result += char
	    
		# Шифрование верхнего регистра
		elif (char.isupper()):
			result += chr((ord(char) - (s + 1040)) % 32 + 1040)

		# Шифрование нижнего регистра
		else:
			result += chr((ord(char) - (s + 1072)) % 32 + 1072)

	return result

direction = input("You want to encrypt text in Caesar's cypher system or decrypt it?\nType 'e' = encode or 'd' to decode.\n")
lang = input("What language it should be?\nType 'e' for English and 'r' for Russian\n")
step = int(input("Give a steps count to rotate the cypher\n"))

text = input("Can you provide me some text to work on?\n")

if direction.lower() == 'e' and lang.lower() == 'e':
	print("Here's a result for your request")
	print(encrypt_eng(text,step))
elif direction.lower() == 'e' and lang.lower() == 'r':
	print("Here's a result for your request")
	print(encrypt_rus(text,step))
elif direction.lower() == 'd' and lang.lower() == 'e':
	print("Here's a result for your request")
	print(decrypt_eng(text,step))
elif direction.lower() == 'd' and lang.lower() == 'r':
	print("Here's a result for your request")
	print(decrypt_rus(text,step))

