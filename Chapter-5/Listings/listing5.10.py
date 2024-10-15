decimal = int(input("Enter a decimal integer: "))

hex = ""

while decimal != 0:
    hexValue = decimal % 16

    if 0 <= hexValue <= 9:
        hexChar = chr(hexValue + ord('0'))
    else:
        hexChar = chr(hexValue - 10 + ord('A'))

    hex = hexChar + hex
    decimal = decimal // 16

print(f"The hex number is {hex}")