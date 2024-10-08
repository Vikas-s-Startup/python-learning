input_number = 1

even_numbers = []
odd_numbers = []
number_of_events = 0

def check_even_odd(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False

def calculate_avg(numbers):
    sum = 0
    for n in numbers:
        sum = sum + int(n)
    average = sum/len(numbers)
    return average

def calculate_sum(numbers):
    sum = 0
    for n in numbers:
        sum = sum + int(n)
    return sum

while int(input_number) != 0:
    input_number = input("Please enter the number, Enter 0 to exit: ")
    if int(input_number) == int(0):
        break
    else:
        if check_even_odd(input_number):
            even_numbers.append(input_number)
        else:
            odd_numbers.append(input_number)
        number_of_events += 1

if number_of_events > 1:
    final_average = calculate_avg(odd_numbers + even_numbers)
    final_sum = calculate_sum(odd_numbers + even_numbers)

    print(f"The number of events {number_of_events}")
    print(f"The number of evens is {len(even_numbers)}")
    print(f"The number of odd is {len(odd_numbers)}")
    print(f"Total is {final_sum}")
    print(f"Average is {final_average}")
else:
    print("0 Entered, Exiting")