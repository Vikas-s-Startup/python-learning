starting_number = 1000
ending_number = 1100
numbers_per_line = 0

for number in range(starting_number, ending_number):
    if number % 11 == 0 or number % 17 == 0:
        print(number, sep= ' ', end=' ')
        numbers_per_line += 1
        if numbers_per_line == 5:
            print("\n")
            numbers_per_line = 0