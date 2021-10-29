import secrets


Words = ["tehran" , "rasht" , "new york" , "texas" , "paris" , "berlin" , "rome" , "london" , "tokyo" ]
hangman_word = secrets.choice(Words)

letter_count = len(hangman_word)


guess = 0



score = letter_count
is_not_win = True


while is_not_win:

	user_guess = input("Emter a Character : ")

	if user_guess == hangman_word :
		print ("Welldone you guess correctly !!!!!")
		break
	else:

		for i in range(0 , letter_count):
			if hangman_word[i] == user_guess:
				guess = i + 1
				if guess != 0:
					print ("the {} in {} palace".format(user_guess , guess))


		if guess == 0 :
			print("We Dont have {} in this word".format(user_guess))

		
		guess = 0
