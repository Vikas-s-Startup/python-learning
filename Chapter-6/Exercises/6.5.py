def displaySortedNumbers(num1, num2, num3):
    smallest_number = min(num1, num2, num3)
    largest_number = max(num1, num2, num3)
    total_sum = num1 + num2 + num3
    middle_number = total_sum - (smallest_number + largest_number)
    print(f"Sorted numbers are {smallest_number}, {middle_number}, {largest_number}")

def main():
    number1 = int(input("Enter number one: "))
    number2 = int(input("Enter number two: "))
    number3 = int(input("Enter number three: "))

    displaySortedNumbers(number1, number2, number3)

main()
