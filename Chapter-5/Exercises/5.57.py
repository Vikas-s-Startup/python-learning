# isbn = input("Enter the first 12-digit of an ISBN number as a string: ")
isbn = "978013213080"
sum_digits = 0
for digit in isbn:
    if int(digit) % 2 == 1:
        sum_digits += int(digit)
    elif int(digit) % 2 == 0:
        sum_digits += 3 * int(digit)
checksum = 10 - (sum_digits % 10)

if checksum == 10:
    new_isbn = str(isbn) + str(0)
else:
    new_isbn = str(isbn) + str(checksum)

print(f"new ISBN {new_isbn}")