# n1 = int(10)
# n2 = int(20)
#
# gcd = int(1)
#
# d = min ( n1, n2)
#
#
# while d >0:
#     if n1 % d == 0 and n2 % d == 0:
#         gcd = d
#     print(d)
#     d -= 1
#
# print(gcd)

def gcd(n1, n2):
    # Find the minimum of the two numbers
    d = min(n1, n2)

    # Loop to find the greatest common divisor
    while d > 0:
        if n1 % d == 0 and n2 % d == 0:
            return d  # Return when the GCD is found
        d -= 1


# Input numbers
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# Find and print the GCD
result = gcd(n1, n2)
print(f"The greatest common divisor of {n1} and {n2} is {result}")