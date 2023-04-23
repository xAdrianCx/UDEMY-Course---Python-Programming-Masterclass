
def  factorial(number: int) -> int:
	"""
	A function that calculates the factorial of the given number as argument.
	:param number: the number to calculate the factorial for.
	:return: factorial number.
	"""
	factorial = 1
	# Check to see if `number` is positive or zero.
	if number == 0:
		return 1
	elif number > 0:
		for i in range(1, number + 1):
			factorial = factorial * i
		return factorial


for i in range(36):
	print(i, factorial(i))