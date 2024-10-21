# Longest common prefix

first_string = "welcomes"
second_string = "welcomes you"

def prefix(s1, s2):
    longest_prefix = ""
    smallest_string = ""
    largest_string = ""

    if len(first_string) > len(second_string):
        smallest_string = second_string
        largest_string = first_string
    elif len(first_string) < len(second_string):
        smallest_string = first_string
        largest_string = second_string

    index = 0
    while index < len(smallest_string):
        if smallest_string[index] != largest_string[index]:
            break
        else:
            longest_prefix += smallest_string[index]
        index += 1

    if len(longest_prefix) > 0:
        print("Largest Prefix is ", longest_prefix)
    else:
        print("Longest Prefix not found")


prefix(first_string, second_string)