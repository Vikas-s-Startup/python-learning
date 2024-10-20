import math
import time

def isPrime(n):
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

def isPalindrome(n):
    # Use string slicing to check if the number is a palindrome
    n_str = str(n)
    return n_str == n_str[::-1]


def main():
    number_of_palindrome_primes = 0
    palindrome_primes_per_line = 0
    starting_number = 1
    while number_of_palindrome_primes < 101:
        starting_number += 1
        if isPrime(starting_number):
            if isPalindrome(starting_number):
                print(starting_number, end=" ")
                palindrome_primes_per_line += 1
                number_of_palindrome_primes += 1
                if palindrome_primes_per_line % 10 == 0:
                    print()
                if number_of_palindrome_primes == 100:
                    break
start_time = time.time()
main()
end_time = time.time() - start_time

print(f"Time Taken is {end_time}")