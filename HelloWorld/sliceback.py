letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

# Create a slice that produces the characters qpo
qpo = letters[-10:-13:-1]
print(qpo)

# Slice the string to produce edcba
edcba = letters[-22::-1]
print(edcba)

# Slice the string to produce the last 8 characters in reverse order
last_8 = letters[25:-9:-1]
print(last_8)