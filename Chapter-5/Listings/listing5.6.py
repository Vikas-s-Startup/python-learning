# Multiplication Table

print("              Multiplication Table")
print("    ", end="")


for i in range(1,11):
    print("  ", i, end='' )
print("\n")

for j in range(1, 11):
    print(j, "  ", end='')
    for n in range(1, 11):
        print("  ", j*n, end= '')
    print("\n")

