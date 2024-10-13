# # Longest common prefix
# stringA = input("Enter a string A")
# stringB = input("Enter a string B")
#
# common_prefix = ""
# smallest_string = ""
# largest_string = ""
#
# if len(stringB) < len(stringA):
#     smallest_string = stringB
#     largest_string = stringA
# elif len(stringA) < len(stringB):
#     smallest_string = stringA
#     largest_string = stringB
# elif len(stringB) == len(stringA):
#     smallest_string = stringB
#     largest_string = stringA
#
# for i in range(len(smallest_string)):
#     if smallest_string[i] == largest_string[i]:
#         common_prefix = common_prefix + smallest_string[i]
#
# print("Common Prefix", common_prefix)


# Longest common prefix
stringA = input("Enter a string A: ")
stringB = input("Enter a string B: ")

# Find the smaller length to avoid redundant comparisons
min_length = min(len(stringA), len(stringB))

# Initialize list to collect common characters
common_prefix_chars = []

# Compare the characters of both strings up to the min_length
for i in range(min_length):
    if stringA[i] == stringB[i]:
        common_prefix_chars.append(stringA[i])
    else:
        break  # Exit loop as soon as characters mismatch

# Join the collected characters into a string
common_prefix = ''.join(common_prefix_chars)

print("Common Prefix:", common_prefix)