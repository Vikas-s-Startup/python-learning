# positive_integer = int(input("Enter a positive Integer: "))
# elements= int(input("Enter the number of elements to pick "))


positive_integer = 6
elements= 2

combinations = 0


for i in range(1, positive_integer+1):
    for j in range(i+1, positive_integer+1):
            print(i,j)
            combinations += 1
print(f"Total Combinations {combinations}")