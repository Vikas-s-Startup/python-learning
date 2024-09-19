import random
number1 = random.randint(1,10)
number2 = random.randint(1, 10)

if number1 < number2:
    number1, number2 = number2, number1

answer = int(input("What is the different between " + str(number1) + "-" + str(number2) + " ?"))

print(f"Provided Answer is {answer}")


while number1 - number2 != answer:
    answer = int(input("Wrong Answer, What is the different between " + str(number1) + "-" + str(number2) + " ?"))

print("\nCorrect Answer Finally!")