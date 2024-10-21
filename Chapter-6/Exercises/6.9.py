def cmsToInches(centimeters):
    return round(2.54 * centimeters, 2)

def inchesToCms(inches):
    return round(inches / 2.54, 2)


centi_list = [1, 3, 5,7,9, 11, 13, 15, 17, 19]
inch_list = [50, 53, 56, 59, 62, 65, 68, 71, 74, 77]

for i in range(0, len(centi_list)):
    print(centi_list[i], " " * 6, inchesToCms(centi_list[i]), end = "         ")
    print(inch_list[i], " " * 6, cmsToInches(inch_list[i]))