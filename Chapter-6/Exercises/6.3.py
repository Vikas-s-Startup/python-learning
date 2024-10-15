


def check_palindrome(string_to_check):
    first_index = 0
    last_index = len(string_to_check) - 1

    is_palindrome = True
    while first_index < last_index:
        if string_to_check[first_index] != string_to_check[last_index]:
            is_palindrome = False
            return is_palindrome
        else:
            first_index += 1
            last_index -= 1
    return is_palindrome

starting_number = input("Enter the starting number: ")
ending_number = input("enter the ending number: ")

for i in range(int(starting_number) , int(ending_number)+1):
    if check_palindrome(str(i)):
        print(i)