data = [
	[7, 9, 5, 2],
	[8, 3, 7, 0],
	[2, 6, 1, 7],
	[3, 9, 7, 5]
]

sum = 0

for i in range(len(data)):
	sum += data[i][i]
print(f"average of diagonal is {sum/4}")
