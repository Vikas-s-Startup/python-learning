def isEven(n):
    is_Even = True
    if int(n)%2 == 1:
        is_Even = False
    return is_Even

def main():
    even_count = 0
    odd_count = 0
    input_numbers = input("Enter a list of integer, separated by commas: ")
    input_numbers = input_numbers.split(", ")
    for number in input_numbers:
        if isEven(number):
            even_count += 1
        else:
            odd_count += 1
    print(f"There are {even_count} even numbers and {odd_count} odd numbers in the list")


main()