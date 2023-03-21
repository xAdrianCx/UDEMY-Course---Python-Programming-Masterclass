def sum_eo(n, t):
	if t.lower() == "e":
		result = sum(i for i in range(n) if i % 2 == 0)
		return result
	elif t.lower() == "o":
		result = sum(i for i in range(n) if i % 2 != 0)
		return result
	else:
		return -1


print(sum_eo(7, "o"))


def sum_eo2(n, t):
	result = 0
	if t.lower() == "e":
		for i in range(n):
			if i % 2 == 0:
				result += i
		return result
	elif t.lower() == "o":
		for i in range(n):
			if i % 2 != 0:
				result += i
		return result
	else:
		return -1

print(sum_eo2(10, "e"))