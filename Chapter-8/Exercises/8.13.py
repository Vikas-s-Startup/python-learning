matrix = [[9, 5, 8], [5, 8, 9], [9, 6, 3]]


def locateSmallest(lst):
	smallest_number = 100000000000
	smallest_row = 0
	smallest_column = 0
	for row in range(len(lst)):
		for column in range(len(lst)):
			if lst[row][column] < smallest_number:
				smallest_number = lst[row][column]
				smallest_row = row
				smallest_column = column

	print(f"Smallest number is {smallest_number} is found at {smallest_row},{smallest_column}")


locateSmallest(matrix)
