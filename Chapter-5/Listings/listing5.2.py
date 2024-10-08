# GuessNumberOneTime.py

import random

system_guess = random.randint(1, 10)

user_guess = int(input("Please guess a number between 1 to 10, that the system might have guessed. "))

while user_guess != system_guess:
    if user_guess > system_guess:
        print("Your guess is too high, try again")
    elif user_guess < system_guess:
        print("your guess is too low, try again")
    user_guess = int(input("Wrong guess, Try again "))

print(f"Correct guess, the answer is {system_guess}")