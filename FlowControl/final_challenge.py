"""
Write a program to print a number of options, and allow the user to select an option from the list.
The options should be numbers from 1 to 9 - although you could use less tan 9 options if you want.
Make sure that there are at least 4 options.
	Example:
		Please choose your option from the list below:
		1. Learn Python
		2. Learn Java
		3. Go swimming
		4. Have dinner
		5. Go to bed
		0. Exit
The program should continue looping, allowing the user to choose one of the options each time around.
The loop should only terminate when the user chooses 0.
If the user makes a valid choice, the program should print a short message.
The message should include the value they typed.
Don't print different messages for each choice - the only thing that should change is the number they typed.
Although you could print out the description, I want to show you a much better way of doing that later.
We're keeping this simple because there are lots of things we haven't covered yet.
If their choice isn't in the menu, nothing should be printed(although you will see their input on the screen).
As an optional extra, modify the program so that the menu is printed again, if they choose an invalid option.
Be careful with that one: you may start off by duplicating the code to print the menu, but it's possible to write the
program without duplicating the print lines.
"""

message = ("""Please choose your option from the list below:
	0. Exit
	1. Play tennis
	2. Stay inside
	3. Make dinner
	4. Draw something
	5. Learn Python
	6. Call someone
	7. Go shopping
	8. Mow the lawn
	9. Watch TV
		""")
print(message)
while True:
	option = input()
	if option == str(0):
		print("You have chosen option: {}. Goodbye!".format(option))
		break
	elif option in "123456789":
		print("You have chosen option: {}.".format(option))
	else:
		print(message)
		