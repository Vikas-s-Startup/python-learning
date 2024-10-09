user_input = int(input("Enter a number between 1 and 15: "))

for i in range(1, user_input+1):
    print("  " * (user_input - i), end="")
    for k in range(i, 1, -1):
        print(k, sep=' ', end = " ")
    for j in range(1, i+1):
        print(j, sep=' ', end = " ")
    print()