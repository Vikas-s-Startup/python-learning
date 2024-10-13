# word reversal

# sentence = input("Enter a sentence")
sentence = "Hello World"

words = sentence.split(" ")

for word in words:
    for char in reversed(word):
        print(char, end = "")
    print(end = " ")