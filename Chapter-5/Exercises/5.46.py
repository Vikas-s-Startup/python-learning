import math

user_input_count = 10
square_sum = 0
total_sum = 0

for i in range(1, user_input_count+1):
    number = float(input(f"Enter {i} number: "))
    total_sum += number
    square_sum += math.pow(number, 2)

# user_input_list = [1, 2, 3, 4.5, 5.6, 6, 7, 8, 9, 10]
# for i in user_input_list:
#     total_sum += i
#     square_sum += math.pow(i, 2)
# print(f"DEBUG total_sum {total_sum}")

mean = total_sum / user_input_count

temporary_result = (square_sum - (math.pow(total_sum, 2)/user_input_count)) / user_input_count
standard_deviation = math.pow(temporary_result, 0.5)

print(f"The mean is {mean}")
print(f"The Standard Deviation is {standard_deviation}")