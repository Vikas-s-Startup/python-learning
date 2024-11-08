import sys


def main():
	data = []
	NUMBER_OF_DAYS = 10
	NUMBER_OF_HOURS = 24

	for day in range(NUMBER_OF_DAYS):
		data.append([])
		for hour in range(NUMBER_OF_HOURS):
			data[day].append([])
			data[day][hour] = []

	for line in sys.stdin:
		line = line.strip()  # Removes trailing newline and spaces
		line = line.strip().split()
		day = int(line[0])-1
		hour = int(line[1])-1
		data[day][hour].append(float(line[2]))
		data[day][hour].append(float(line[3]))

	for day in data:
		print(f'DAYYYYYYYYYYYYYYYYYY {data.index(day)}')
		day_temperature = 0
		day_humidity = 0
		for hour in day:
			# print(hour)
			day_temperature += hour[0]
			day_humidity += hour[1]
		print(f"Day {data.index(day)}'s average temperature is {day_temperature/24}")
		print(f"Day {data.index(day)}'s average Humidity is {day_humidity/24}")
		print("----------------------------------------")


if __name__ == '__main__':
	main()
