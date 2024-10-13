# decimal to integer
import math

# To convert integer to binary, start with the integer in question
# and divide it by 2 keeping notice of the quotient and the remainder.
# Continue dividing the quotient by 2 until you get a quotient of zero.
# Then just write out the remainders in the reverse order.


# user_input = int(input("Enter a decimal Integer: "))

user_input = 343123298

quotient = user_input
binary_representation = ""

while int(quotient) > 0:
    remainder = str(quotient % 2)
    binary_representation += str(remainder)
    quotient = quotient // 2

    print(quotient, remainder)


print(binary_representation)

