# String Prefix Tester

# first_string = input("Enter the first string: ")
# second_string = input("Enter the second string: ")

first_string = "Hello"
second_string = "Hello World"

# first_string = "Hello Cat"
# second_string = "Hello Dog"

match_found = True
for i in range(0, len(first_string)):
    if first_string[i] != second_string[i]:
        match_found = False
        break

print("Match Found") if match_found else print("Match Not found")