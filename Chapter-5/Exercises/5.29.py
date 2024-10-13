def is_leap_year(year):
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

total_num_leap_years = 0
for year in range(2001, 2100):
    if is_leap_year(year):
        total_num_leap_years += 1
        print(year, end=" ")

print(f"\nTotal Leap Years {total_num_leap_years}")