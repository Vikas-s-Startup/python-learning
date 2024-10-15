def printMonth(year, month):
    printMonthTitle(year, month)
    printMonthBody(year, month)

def printMonthTitle(year, month):
    print("          ", printMonthName(month)," ", year)
    print("---------------------------------")
    print(" Sun Mon Tue Wed Thru Fri Sat")

def printMonthBody(year, month):
    startDay = getStartDay(year, month)
    numberofDaysInMonth = getNumberOfDaysInMonth(year, month)

    i = 0
    for i in range(startDay):
        print("    ", end = "")
    for i in range(1, numberofDaysInMonth + 1):
        print(f"{i:4d}", end = "")
        if (i+startDay) % 7 ==0:
            print()

def printMonthName(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'

def getStartDay(year, month):
    START_DAY_FOR_JAN_1800 = 3
    totalNumberOfDays = getTotalNumberofDays(year, month)

    return ( START_DAY_FOR_JAN_1800 + totalNumberOfDays ) % 7

# get the total number of days since Jan 1 1800
def getTotalNumberofDays(year, month):
    total = 0
    for i in range(1800, year):
        if isLeapYear(i):
            total += 366
        else:
            total += 365

    for j in range(1, month):
        total += int(getNumberOfDaysInMonth(year, j))

    return total

def getNumberOfDaysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        return 29 if isLeapYear(year) else 28

def isLeapYear(year):
    return year% 400 == 0 or (year % 4 == 0 and year % 100 !=0)

def main():
    year = int(input("Enter full year (example 2002): "))
    month = int(input("Enter month as number between 1 and 12: "))

    printMonth(year, month)

main()