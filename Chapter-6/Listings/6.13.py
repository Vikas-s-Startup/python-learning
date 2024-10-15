def printMonth(year, month):
    printMonthTitle(year, month)
    printMonthBody(year, month)

def printMonthTitle(year, month):
    print("          ", printMonthName(month)," ", year)
    print("---------------------------------")
    print(" Sun Mon Tue Wed Thu Fri Sat")  # corrected typo from "Thru" to "Thu"

def printMonthBody(year, month):
    startDay = getStartDay(year, month)
    numberofDaysInMonth = getNumberOfDaysInMonth(year, month)

    i = 0
    for i in range(startDay):
        print("    ", end = "")  # 4 spaces for each day
    for i in range(1, numberofDaysInMonth + 1):
        print(f"{i:4d}", end = "")
        if (i + startDay) % 7 == 0:
            print()

def printMonthName(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    return months[month - 1]

def getStartDay(year, month):
    START_DAY_FOR_JAN_1800 = 3  # Jan 1, 1800 was a Wednesday
    totalNumberOfDays = getTotalNumberofDays(year, month)

    return (START_DAY_FOR_JAN_1800 + totalNumberOfDays) % 7

def getTotalNumberofDays(year, month):
    total = 0
    # Add days for years since 1800
    for i in range(1800, year):
        if isLeapYear(i):  # check each year in the range for leap year
            total += 366
        else:
            total += 365

    # Add days for months in the current year
    for j in range(1, month):
        total += getNumberOfDaysInMonth(year, j)

    return total

def getNumberOfDaysInMonth(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if isLeapYear(year) else 28

def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    year = int(input("Enter full year (example 2002): "))
    month = int(input("Enter month as number between 1 and 12: "))

    printMonth(year, month)

main()
