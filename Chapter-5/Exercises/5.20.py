user_input = 6

print("\n Pattern 1")
for i in range(1, user_input+1):
    for j in range(1, i+1):
        print(j, sep=' ', end = " ")
    print()


print("\n Pattern 2")
for i in range(user_input+1, 1 , -1):
    for j in range(1, i):
        print(j, sep=' ', end = " ")
    print()

print("\nPattern 3")
for i in range(1, user_input+1):
    print("  " * (user_input - i), end="")
    for k in range(i, 0, -1):
        print(k, sep=' ', end = " ")
    print()

print("\nPattern 4")
for i in range(1, user_input + 1):
    print("  " * i, end="")
    for j in range(i, user_input + 1):
        print(j, sep=" ", end=" ")
    print()
