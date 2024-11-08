# user_input_string = str(input("Please enter a sentence: ")).split(" ").lstrip().rstrip()
user_input_string = "VIKAS IS HERE DOING GREAT"
user_input_string = user_input_string.lstrip().rstrip().split(" ")
print(user_input_string)
for i in range(len(user_input_string)):
    for j in range(i + 1, len(user_input_string)):
        print(user_input_string[i], user_input_string[j])