
parrot = "Norwegian Blue"

# # String slicing
# print(parrot[0:6])      # Norweg
# print(parrot[3:5])      # weg
# print(parrot[0:9])      # Norwegian
# print(parrot[:9])       # Norwegian
# print(parrot[10:14])    # Blue
# print(parrot[10:])      # Blue

# # Negative slicing
# print(parrot[-4:-2])        # Bl
# print(parrot[-4:12])        # Bl
# print(parrot[::-1])         # reverse the string

# Step in slicing
print(parrot[0:6:2])        # Nre
print(parrot[0:6:3])        # Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

# Remove separators in a string
values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print([int(val) for val in values])

print("________________________________")
values2 = "".join(i if i not in separators else " " for i in number)
print(values2)
print("__________________________________")
