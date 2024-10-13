y = input("Enter a year: ")
first_day = input("Enter the first day of the year: ")
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def is_leap_year(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if is_leap_year(y):
    print(f"User Provided year {y} is a leap year, hence days in year 366 and February has 29 days")
    days_in_months[1] = 29
else:
    print(f"User Provided year {y} is  not a leap year, hence days in year 365 and February has 28 days")

current_day = first_day

for month in range(12):
    print(f"First day of month {month + 1} is {days_of_week[int(current_day)]}")
    current_day = (int(current_day) + int(days_in_months[month])) % 7
