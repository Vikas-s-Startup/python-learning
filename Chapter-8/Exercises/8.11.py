color_map = {
	'0': 'R',
	'1': 'B',
	'2': 'G'
}


def decimal_to_ternary(n):
	n = int(n)
	if n == 0:
		return "0"

	ternary = ""
	while n > 0:
		remainder = n % 3
		ternary = str(remainder) + ternary
		n //= 3
	return ternary


number = decimal_to_ternary(7)

ternary_number = decimal_to_ternary(number).zfill(16)

for index in range(1, len(ternary_number) + 1):
	print(color_map[ternary_number[index - 1]], end=' ', sep=' ')
	if index % 4 == 0:
		print()
