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

c = 2
while c <= 10:
    value = math.pow(2, c) - 1
    if isPrime(value):
        print(c, "     ", value)
    c+=1