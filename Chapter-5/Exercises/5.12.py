starting_number = int(input("Enter Starting number: "))
ending_number = int(input("Enter Ending number: "))
numbers_per_line = 0

for number in range(starting_number, ending_number):
    if number % 3 ==0 and number % 7 == 0:
        print(number, sep= ' ', end=' ')
        numbers_per_line += 1
        if numbers_per_line == 5:
            print("\n")
            numbers_per_line = 0
