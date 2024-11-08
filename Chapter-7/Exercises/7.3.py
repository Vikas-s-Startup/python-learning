input_string = input("Enter a list of strings Separated by Spaces: ").strip().split(" ")

unique_words = []

for word in input_string:
    if word not in unique_words:
        unique_words.append(word)

for unique_word in unique_words:
    print(f"Count of {unique_word}: {input_string.count(unique_word)}")