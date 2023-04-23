
def fizz_buzz(number: int) -> str:
	"""
	Fizz Buzz Game.
	:return:"fizz" if the number is divisible by 3.
			"buzz" if the number is divisible by 5.
			"fizz_buzz" if the number is divisible by both 3 and 5.
			the number as a string if the number isn't divisible by either 3 or 5.
	"""

	if (int(number) % 3 == 0) and (int(number) % 5 == 0):
		return "fizz buzz"
	elif number % 3 == 0:
		return "fizz"
	elif number % 5 == 0:
		return "buzz"
	else:
		return str(number)


input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
	next_number += 1
	print(fizz_buzz(next_number))
	next_number += 1
	correct_answer = fizz_buzz(next_number)
	players_answer = input("Your go: ")
	if players_answer != correct_answer:
		print("You lose, the correct answer was {}".format(correct_answer))
		break
else:
	print("Well done, you reached {}".format(next_number))
