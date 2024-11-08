import random

words_list = ["vikas", "koppineedi", "tamil", "telugu"]


def guess_word_game():
	random_word_index = random.randint(0, len(words_list) - 1)
	random_word = words_list[random_word_index]
	guess_word = ''
	num_of_bad_guess = 0
	while guess_word != random_word:
		for character in random_word:
			guess_character = ''
			while guess_character != character:
				guess_character = str(
					input(f"Enter a letter in word {guess_word}{'*' * (len(random_word) - len(guess_word))} > "))
				num_of_bad_guess += 1
			guess_word += guess_character
	print(f"The word is {random_word}, and you missed {num_of_bad_guess} times. ")


def main():
	continue_playing = "y"
	while continue_playing != "n":
		guess_word_game()
		continue_playing = input("Do you want to guess another word? Enter Y or N > ")
	print("Thanks for playing hangman game developed by soon legendary programmer Vikas Koppineedi")


main()
