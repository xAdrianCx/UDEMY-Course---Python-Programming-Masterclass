""" Write a small program to ask for a name and an age.

When both values have benn entered, check if the person is the right age to go on an 18-30 
holiday(they must be over 18 and under 30).

if the are, welcome them to the holiday, otherwise print a (polite) message refusing them entry.

Our program expect valid input. We'll see how to handle invalid numbers, later in the course."""

name = input("Please enter your name: ")
age = int(input("Enter your age: "))
if name != "" and (age >= 18 and age < 31) :
	print("Hello, {} and welcome to our holiday!".format(name))
else:
	if name == "":
		print("You forgot to enter your name.")
		name = input("Please enter your name: ")
		if name == "":
			print("Seems that you don't want to enter your name, so you can't enter the holiday. Goodbye!")
	else:
		print("Your age is not suitable for this holiday. Goodbye!")