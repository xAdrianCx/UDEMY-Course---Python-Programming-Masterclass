
def multiply(x, y):
	"""
	A function that multiplies 2 numbers.
	:return:
	"""
	result = x * y
	return result


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
	two_times = multiply(2, val)
	print(two_times)