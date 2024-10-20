import math

def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # skip even numbers greater than 2
    # Check divisibility from 3 up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

l = 0

first_prime = 2
for j in range(3, 1001, 2):
    if isPrime(j):
        next_prime = j
        if next_prime - first_prime == 2:
            print(first_prime, next_prime, )
        first_prime = next_prime