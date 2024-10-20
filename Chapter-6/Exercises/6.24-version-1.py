import time


def isPrime(n):
    is_Prime=True
    for i in range(2,n-1):
        if n % i ==0:
            is_Prime=False
            break
    return is_Prime

def isPalindrome(string):
    string = str(string)
    first_index = 0
    last_index = len(string) - 1
    is_palindrome = True
    while first_index < last_index:
        if string[first_index] != string[last_index]:
            is_palindrome = False
            break
        else:
            first_index += 1
            last_index -= 1
    return is_palindrome


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