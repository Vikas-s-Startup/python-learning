# Checking for palindrome.

string = "vikasakiv"
length = len(string)
low = 0
high = length - 1
is_palindrome = True

while low< high:
    if string[low] != string[high]:
        is_palindrome = False
    low +=1
    high -= 1

print(f"given string {string} is {is_palindrome}")

