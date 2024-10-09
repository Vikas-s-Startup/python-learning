import math

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

total_prime_numbers = 0
numbers_per_line = 10

for i in range(1000,2001):
    if is_prime(i):
        total_prime_numbers += 1
        print(i, end=" ")
        numbers_per_line -= 1
        if numbers_per_line == 0:
            numbers_per_line=10
            print()