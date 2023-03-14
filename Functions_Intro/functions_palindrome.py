
def is_palindrome(string):
	"""
	Checks if a string is palindrome
	:param string: a string to check if it's a palindrome(reads the same from left to right, as from right to left).
	:return: True if the string is a palindrome, else False.
	"""
	# backwards = str[::-1]
	# return backwards == string
	return string[::-1].casefold() == string.casefold()



def palindrome_sentence(sentence):
	"""
	Checks if a sentence is a palindrome.
	:param sentence: sentence to be checked if it's a palindrome.
	:return: True if it's a palindrome, False if not.
	"""
	string = "".join(i for i in sentence if i.isalnum())
	# return new_word.casefold() == new_word[::-1].casefold()
	return is_palindrome(string)


sent = "Do geese see god?"
if palindrome_sentence(sent):
	print(f"{sent} is a palindome")
else:
	print(f"{sent} is not a palindrome")
