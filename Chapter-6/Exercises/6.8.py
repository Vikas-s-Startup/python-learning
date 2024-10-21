def celsiusToFahrenheit(celsius):
    return round((9 / 5) * celsius + 32, 3)


def fahrenheitToCelsius(fahrenheit):
    return round((5 / 9) * (fahrenheit - 32), 3)


# print(celsiusToFahrenheit(40))

def printProgramHeader():
    print("Celsius      Fahrenheit     |     Fahrenheit               Celsius")


celsius_list = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31]
fahrenheit_list = [120, 110, 100, 90, 80, 70, 60, 50, 40, 30]

printProgramHeader()
for i in range(0, len(celsius_list)):
    print(celsius_list[i], "           ", celsiusToFahrenheit(celsius_list[i]), "     |     ", end = "")
    print(fahrenheit_list[i], "      ", fahrenheitToCelsius(fahrenheit_list[i]))
