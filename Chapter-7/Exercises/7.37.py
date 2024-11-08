import math


def is_perfectSquare(number):
	value = math.pow(number, 0.5)
	decimal_value = int(str(value).split(".")[1])
	if decimal_value != 0:
		return False
	else:
		return True


def main():
	# m = int(input("Enter an integer m: "))
	m = 12
	smallest_number_n = 1
	for i in range(1, m + 1):
		if is_perfectSquare(i * m):
			smallest_number_n = i
			break
	print(
		f"The smallest number n for m * n to be a perfect square is {smallest_number_n} , where m * n is {12 * smallest_number_n}")


main()
