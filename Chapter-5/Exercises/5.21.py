import math

user_input = 9
for i in range(0, user_input):
    print("  " * (user_input - i), end=" ")
    for k in range(0, i,):
        print(int(math.pow(2, k)), sep=' ', end=" ")
    for p in range(i-2, -1, -1):
        print(int(math.pow(2, p)), sep=' ', end = " ")
    print()