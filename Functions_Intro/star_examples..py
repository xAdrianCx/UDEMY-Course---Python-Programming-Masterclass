numbers = (0, 1, 2, 3, 4, 5)

# # Star(*) used to unpack a sequence. Any sequence can be unpacked.
# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args):
	print(args)
	for x in args:
		print(x)


test_star(1, 2, 3, 4, 5)

print()
test_star()

