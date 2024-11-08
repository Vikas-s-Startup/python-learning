# data = []
# number_of_rows = 3
# number_of_columns = 4
#
# for row in range(number_of_rows):
# 	data.append([])
# 	for column in range(number_of_columns):
# 		n = int(input(f"Enter a a digit to input into {number_of_rows}-by-{number_of_columns} Row {row}, Column {column}: "))
# 		data[row].append(n)

data = [
	[12, 63, 59, 82],
	[75, 65, 92, 52],
	[41, 73, 63, 88],
]
print(data)

for v in range(4):
	print(max(data[0][v], data[1][v], data[2][v]))

