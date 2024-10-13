# Program that displays the first fifty prime numbers in five lines, each containing ten numbers.
import math

prime_number_count = 0
prime_numbers_per_line = 0
max_number_of_lines = 5
max_prime_numbers = 50
init_number = 1

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # All other even numbers are not prime
    # Check only odd numbers up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

while prime_number_count <= max_prime_numbers:
    prime_numbers_per_line = 0
    while prime_numbers_per_line < 10:
        if is_prime(init_number):
            print(init_number, end = ' ')
            prime_number_count += 1
            prime_numbers_per_line += 1
        init_number +=1
    print()
