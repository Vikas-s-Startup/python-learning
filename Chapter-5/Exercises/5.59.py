vowels = ["a", "e", "i", "o", "u"]
sentence = "Hello World"

words = 0
vowels_count = 0
constants = 0

print(f"Number of words: {len(sentence.split(" "))}")

for char in sentence:
    if char in vowels:
        vowels_count +=1
    elif char != " ":
        constants +=1

print(f"Number of vowels: {vowels_count}")
print(f"Number of constants: {constants}")
