# String Twister
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")
#
# first_string = "ABCDEFGH"
# second_string = "abcd"

def create_concatenated_twisted_string(firststring, secondstring):
    final_string = ""
    max_length = max(len(firststring), len(secondstring))

    for char in range(max_length):
        if char < int(len(firststring)):
            final_string += firststring[char]
        if char < int(len(secondstring)):
            final_string += secondstring[char]
    return final_string

twisted_concatenated_string = create_concatenated_twisted_string(first_string, second_string)

print(f"the Concatenated twisted string is {twisted_concatenated_string}")
print("Enjoyyyy Pandagoooooo!")
