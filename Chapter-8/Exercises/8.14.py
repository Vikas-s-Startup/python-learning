import random


def generate_matrix(n):
	return [[random.choice(['1', '0']) for _ in range(n)] for _ in range(n)]


def print_matrix(board):
	print("--------Matrix--------")
	for row in board:
		print("|", end=" ")
		for cell in row:
			print(cell, "|", end=" ")
		print()
	print("\n"*2)


def all_elements_equal(lst):
	return len(set(lst)) <= 1


def row_check(matrix):
	for row in range(len(matrix)):
		if all_elements_equal(matrix[row]):
			print("Same numbers on a row")
			break
	print("no same numbers on a row")


def column_check(matrix):
	for col in range(len(matrix[0])):
		column_elements = [matrix[row][col] for row in range(len(matrix))]
		if all_elements_equal(column_elements):
			print("Same numbers in column", col)
			break
	print("no same numbers on a column")


def major_diagonal_check(matrix):
	diagonal_numbers = []
	n = len(matrix)
	row = 0
	col = 0
	while row < n and col < n:
		diagonal_numbers.append(matrix[row][col])
		row += 1
		col += 1
	if all_elements_equal(diagonal_numbers):
		print("Same numbers in major diagonal")
		return
	print("No same numbers on a diagonal")


def sub_diagonal(matrix):
	sub_diagonal_numbers = []
	n = len(matrix)
	row = 1
	col = 0
	while row < n and col < n:
		sub_diagonal_numbers.append(matrix[row][col])
		row += 1
		col += 1
	if all_elements_equal(sub_diagonal_numbers):
		print("Same numbers in Sub diagonal")
		return
	print("No same numbers on a Sub diagonal")


def main():
	m_size = int(input("Enter the length of a square matrix: "))
	matrix = generate_matrix(m_size)
	print_matrix(matrix)
	row_check(matrix)
	column_check(matrix)
	major_diagonal_check(matrix)
	sub_diagonal(matrix)



# no same numbers on a row
# no same numbers on a column
# no same numbers on the major diagonal
# no same numbers on the sub-diagonal.

main()
