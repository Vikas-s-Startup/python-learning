import random

number_of_random_numbers = int(input("Enter the number of integers to generate: "))

random_numbers_generated_count = 0
random_numbers = []

while random_numbers_generated_count < number_of_random_numbers:
    random_numbers.append(random.randint(1, 100))
    random_numbers_generated_count += 1

print(f"{number_of_random_numbers} random numbers are {random_numbers}")
print("Max Number is ", max(random_numbers))
print("Min Number is ", min(random_numbers))

sum = 0
for i in random_numbers:
    sum += i

print("Average of the above random numbers is ", sum/len(random_numbers))