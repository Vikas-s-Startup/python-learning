original_list = input("Enter ten numbers: ").strip().replace(" ", "").split(" ")

distinct_numbers = []

for number in original_list:
    if number not in distinct_numbers:
        distinct_numbers.append(number)

print("Number of Distinct numbers are ", len(distinct_numbers))
print("Distinct numbers are ", distinct_numbers)