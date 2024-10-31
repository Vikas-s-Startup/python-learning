stringOne = "silent"
stringTwo = "listen"

stringOne = list(stringOne)
stringTwo = list(stringTwo)

stringOne.sort()
stringTwo.sort()

if stringOne == stringTwo:
    print("Yes they are anagrams")
else:
    print("not anagrams")