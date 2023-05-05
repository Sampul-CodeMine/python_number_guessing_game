#!/usr/bin/python3

"""A simple Number Guessing Game in Python Programming Language"""

def generator() -> list:
	"""A function that generates 3 numbers usin the random class
	Return:
	    (list) - A list of integer values
	"""
	from random import randint as r
	low = r(1, 100)
	high = r(100, 1000)
	to_guess = r(low, high)
	return [low, high, to_guess]

def accept_value() -> int | None:
	"""A function that accepts value from the user.
	Return:
	    (int) if the data entered is of type integer
		(None) if the data is empty or not numeric
	Raises:
	    ValueError: if no data is supplied or not numeric
	    (KeyboardInterrupt, EOFError): if CTRL+Z or CTRL+C is clicked
	"""
	while True:
		try:
			return int(input("Guess Number: "))
		except Exception as err:
			print("Please provide a numeric data.")
			return
		except (KeyboardInterrupt, EOFError):
			print("\nProgram was interrupted.")
			exit(1)

def starter() -> None:
	"""This is the program Logic"""
	low, high, to_guess = generator()
	prompt = f"""
	Welcome to Number Guessing Game Using Python Programming Language
	==================================================================
	
	Guess a number between {low} and {high}
	"""
	counter = 0
	is_found = False
	print(prompt)
	while is_found is False:
		counter += 1
		your_guess = accept_value()
		if your_guess is None:
			print("")
			continue
		if your_guess > to_guess:
			print(f"{your_guess} is larger.\n")
		elif your_guess < to_guess:
			print(f"{your_guess} is smaller.\n")
		else:
			is_found = True
			break
	if is_found is True and counter <=3:
		print(f"Genius! You found {to_guess} after {counter} guess(es).")
	elif is_found is True and counter <= 10:
		print(f"Good! You found {to_guess} after {counter} guesses.\n")
	else:
		print(f"Not a bad try. {to_guess} was found after {counter} guesses.\n")
		exit(0)

if __name__ == "__main__":
	starter()