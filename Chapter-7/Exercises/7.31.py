def count(string):
	count_of_characters = {}
	for c in string:
		if c not in count_of_characters.keys():
			count_of_characters[c] = 1
		else:
			count_of_characters[c] += 1
	return count_of_characters


def main():
	user_input = input("Enter a string: ")
	count_map = count(user_input)
	for key, value in count_map.items():
		print(f"{key} occurs {value} times")


main()
