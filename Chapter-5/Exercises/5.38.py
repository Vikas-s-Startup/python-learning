stringA = input("Enter a string A")
stringB = input("Enter a string B")

common_prefix = ""
smallest_string = ""
largest_string = ""

if len(stringB) < len(stringA):
    smallest_string = stringB
    largest_string = stringA
elif len(stringA) < len(stringB):
    smallest_string = stringA
    largest_string = stringB
elif len(stringB) == len(stringA):
    smallest_string = stringB
    largest_string = stringA

for i in range(len(smallest_string)):
    if smallest_string[i] == largest_string[i]:
        common_prefix = common_prefix + smallest_string[i]

print("Common Prefix", common_prefix)