string = "abcdefghijklmnopqrstuvwxyz"
# Reverse order
print(string[::-1])

# Get the n last characters in a string.
print(string[-5:])

# Get the last item in a string.
print(string[-1:])

# Get the 1st character in a string.
print(string[:1])   # this returns an empty string if there no item at position 0.
print(string[0])  # This throws an index error if there's no item at position 0.
