# # Get the squares and cubes of some numbers.
# for i in range(1, 13):
#     print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

# # Formatting width of the columns for better visuals.
# for i in range(1, 13):
#     print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# # Aligning the values on the left side.
# for i in range(1, 13):
#     print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

# # Center the values.
# for i in range(1, 13):
#     print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

# Get some digits of Pi.
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:<12f}".format(22 / 7))
print("Pi is approximately {0:<12.50f}".format(22 / 7))
print("Pi is approximately {0:<52.50f}".format(22 / 7))
print("Pi is approximately {0:<62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

print("{0:<5.5f}".format(22//7))