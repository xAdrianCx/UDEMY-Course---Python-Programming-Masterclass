
"""
We call an onject 'immutable' in Python if it can't be changed.
Built-in immutable objects in Python:
	- int (integer)
	- float (decimal)
	- bool(True and False): a subclass of int
	- str (string)
	- tuple
	- frozenset
	- bytes
"""

# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result))
