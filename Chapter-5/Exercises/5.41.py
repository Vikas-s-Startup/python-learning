integer = int(input("Enter an integer (0: for end of input)"))

maximum = integer
count = 1

while integer !=0:
    integer = int(input("Enter an integer (0: for end of input)"))

    if integer > maximum:
        maximum = integer
        count = 1
    elif integer == maximum:
        count += 1


print(f"Max number is {maximum} and count is {count}")