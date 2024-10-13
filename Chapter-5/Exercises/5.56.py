sentence = input("Enter a sentence: ")
word_count_map = {}
for i in sentence.split(" "):
    if i in word_count_map.keys():
        word_count_map[i] += 1
    else:
        word_count_map[i] = 1

print("Word Frequency:")
for key, value in word_count_map.items():
    print(key, ": ", value)