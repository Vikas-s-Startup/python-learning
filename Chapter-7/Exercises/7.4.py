first_list = input("Enter the first list of integers separated by space").strip().split(" ")
second_list = input("Enter the second list of integers separated by space").strip().split(" ")

# assuming both lists are of equal length

common_numbers = []
for number in first_list:
    if number in second_list:
        common_numbers.append(number)

print("Common numbers are: ", common_numbers)