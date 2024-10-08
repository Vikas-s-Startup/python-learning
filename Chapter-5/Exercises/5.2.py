import random
import time


start_time = time.time()
question = 1
correct_answers = 0
wrong_answers = 0

while question <= 10:
    numb1 = random.randint(1, 10)
    numb2 = random.randint(1, 10)

    if numb1 < numb2:
        numb1, numb2 = numb2, numb1

    expected_answer = numb1 - numb2

    user_answer = input(f"Please guess the difference between {numb1} and {numb2}: ")

    if int(user_answer) == int(expected_answer):
        correct_answers +=1
    else:
        wrong_answers += 1

    question += 1

end_time= time.time()

total_time = end_time-start_time

print(f"Total Time taken to finish the test: {total_time}, correct answers: {correct_answers}, wrong answers {wrong_answers}")


