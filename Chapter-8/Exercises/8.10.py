import random


def generate_matrix():
	return [[random.choice(['1', '0']) for _ in range(5)] for _ in range(5)]


def print_matrix(board):
	print("----------------Matrix-----------------")
	for row in board:
		print("|", end=" ")
		for cell in row:
			print(cell, "|", end=" ")
		print()


def main():
	matrix = generate_matrix()
	print_matrix(matrix)
	colum_count = []
	row_count = []
	for row in matrix:
		row_count.append(row.count('1'))

	for column in range(5):
		c_count = 0
		for row in range(5):
			# print(matrix[row][column])
			if matrix[row][column] == '1':
				c_count += 1
		colum_count.append(c_count)

	print(f"Column Count {colum_count}")
	print(f"Row count {row_count}")

	print(f"The smallest Row index : {row_count.index(min(row_count))}")
	print(f"The smallest Column Index : {colum_count.index(min(colum_count))}")


main()
