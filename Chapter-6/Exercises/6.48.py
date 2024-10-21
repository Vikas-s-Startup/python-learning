# user_integer = input("Enter an integer: ")
# user_width = input("Enter the width: ")

user_integer = "235"
user_width = "6"

user_integer_length = len(user_integer)

prefixZeros = ""

if user_integer_length > int(user_width):
    formatted_number = user_integer
else:
    required_zeros = int(user_width) - user_integer_length
    for z in range(0, required_zeros):
        prefixZeros = str("0") + str(prefixZeros)
    formatted_number = prefixZeros + user_integer

print(f"The formatted number is {formatted_number}")