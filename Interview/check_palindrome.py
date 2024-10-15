string_to_check = "Step on no pets"
string_to_check = string_to_check.replace(" ", "").lower()
first_index = 0
last_index = len(string_to_check) - 1

is_palindrome = True
while first_index < last_index:
    if string_to_check[first_index] != string_to_check[last_index]:
        is_palindrome = False
        break
    else:
        first_index += 1
        last_index -= 1

print(is_palindrome)
