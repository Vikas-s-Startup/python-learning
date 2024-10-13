import random
import time

NUMBER_OF_QUESTIONS = 5
CURRENT_QUESTION = 0

CORRECT_ANSWERS = 0
WRONG_ANSWERS = 0

start_time = time.time()

while CURRENT_QUESTION < NUMBER_OF_QUESTIONS:
    number1 = random.randint(1,10)
    number2 = random.randint(1, 10)

    if number1 < number2:
        number1, number2 = number2, number1

    system_answer = number1 - number2
    user_answer = int(input("Next Question, What is the different between " + str(number1) + "-" + str(number2) + " ?"))
    print(f"User Answer is {user_answer} and System Answer is {system_answer}")

    if system_answer == user_answer:
        CORRECT_ANSWERS = CORRECT_ANSWERS + 1
        print("your answer is correct \n")
    else:
        WRONG_ANSWERS = WRONG_ANSWERS + 1
        print("Your answer is wrong \n")

    CURRENT_QUESTION = CURRENT_QUESTION + 1

end_time = time.time()

time_taken = end_time-start_time

print(f"\nCorrect answers are {CORRECT_ANSWERS} and wrong answers are {WRONG_ANSWERS} and time taken to answer is {time_taken}")