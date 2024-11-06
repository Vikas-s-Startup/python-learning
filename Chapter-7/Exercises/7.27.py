from operator import index


def hasConsecutiveChat(string):
    lst = list(string)
    foundConsecutiveCharacters = False
    for char in range(0, len(lst)-1):
        if lst[char] == lst[char+1]:
            foundConsecutiveCharacters = True
    return foundConsecutiveCharacters


if hasConsecutiveChat("python"):
    print("The string has Consecutive Characters")
else:
    print("The string has no consecutive Characters")
