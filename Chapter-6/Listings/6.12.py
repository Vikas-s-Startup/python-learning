def main():
    hex_value = input("Enter a hex number: ").rstrip()

    decimal_value = hexToDecimal(hex_value.upper())

    if decimal_value is None:
        print("Incorrect Hex number")
    else:
        print(f"The decimal value for hex number {hex_value} is {decimal_value}")


def hexToDecimal(hex_value):
    decimal_value = 0
    for hex_char in hex_value:
        if 'A' <= hex_char <= 'F' or '0' <= hex_char <= '9':
            decimal_value = decimal_value * 16 + hexChar2Dec(hex_char)
        else:
            return None
    return decimal_value


def hexChar2Dec(ch):
    if 'A' <= ch <= 'F':
        return 10 + ord(ch) - ord('A')
    else:
        return ord(ch) - ord('0')


main()
