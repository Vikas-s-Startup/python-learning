import math
import time


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

# n_str[::-1]

def main():
    emirp = 0
    emirp_per_line = 0
    starting_number = 1
    while emirp_per_line < 101:
        starting_number += 1
        if isPrime(starting_number):
            starting_number = str(starting_number)
            reverse_number = starting_number[::-1]
            if isPrime(reverse_number):
                print(starting_number, end=" ")
                emirp_per_line += 1
                if emirp_per_line % 10 == 0:
                    print()
            starting_number = int(starting_number)

start_time = time.time()
main()
end_time = time.time() - start_time

print(f"Time Taken is {end_time}")