# user_input_list = input("Please enter the list of integers seperated by space")
user_input_list = "2 1 21 89 23 12 3 4 5 93"
user_input_list = user_input_list.lstrip().rstrip().split(" ")
user_input_list = [int(x) for x in user_input_list]


pivot = user_input_list[0]
final_list = []
for item in user_input_list:
    if item < pivot:
        final_list.append(item)
for item in user_input_list:
    if item == pivot:
        final_list.append(item)
for item in user_input_list:
    if item > pivot:
        final_list.append(item)

print(final_list)