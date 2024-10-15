def isPrime(number):
    divisor = 2
    while divisor <= number/2:
        if number % divisor == 0:
            return False
        divisor+=1
    return True

number_of_primes_required = 50

number_of_primes_per_line = 0

count = 0
i = 2
while count < 50:
    if isPrime(i):
        print(i, end=" ")
        count += 1
        number_of_primes_per_line += 1
        if number_of_primes_per_line == 10:
            print()
            number_of_primes_per_line = 0
    i += 1
