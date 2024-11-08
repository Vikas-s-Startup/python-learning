from itertools import count
from random import randint

input_list = input("Enter a list of integers:").strip().split(" ")
random_number = str(randint(1, 10))
random_number_count = input_list.count(random_number)

print("Generated Random number is ", random_number, " and number of occurrences are ", random_number_count)