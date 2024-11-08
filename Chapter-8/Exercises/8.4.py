employee_hour_data = [
	[2, 4, 3, 4, 5, 8, 8],
	[7, 3, 4, 3, 3, 4, 4],
	[3, 3, 4, 3, 3, 2, 2],
	[9, 3, 4, 7, 3, 4, 1],
	[3, 5, 4, 3, 6, 3, 8],
	[3, 4, 4, 6, 3, 4, 4],
	[3, 7, 4, 8, 3, 8, 4],
	[6, 3, 5, 9, 2, 7, 9]
]

avgs = []
for employee in employee_hour_data:
	avg_hours = 0
	for hour in employee:
		avg_hours += hour
	average = avg_hours/len(employee)
	avgs.append(average)
	print(f"Employee {employee_hour_data.index(employee)} average is {average}")

avgs.sort()

print(avgs[::-1])


