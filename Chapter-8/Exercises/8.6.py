matrix_a = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

matrix_b = [
	[0, 2, 4],
	[1, 4.5, 2.2],
	[1.1, 4.3, 5.2]
]

matrix_c = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]


def calculate_c_index(i, j):
	return (matrix_a[i][0] * matrix_b[0][j]) + (matrix_a[i][1] * matrix_b[1][j]) + (matrix_a[i][2] * matrix_b[2][j])


for row in range(len(matrix_c)):
	for column in range(len(matrix_c[row])):
		matrix_c[row][column] = calculate_c_index(row, column)

print(matrix_c)
