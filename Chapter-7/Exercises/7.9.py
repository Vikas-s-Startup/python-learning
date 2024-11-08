import math


def deviation(lst, msean):
    temp = 0
    for x in lst:
        temp += math.pow((x - msean), 2)
    temp = temp/(len(lst)-1)
    return math.pow(temp, 0.5)


def mean(lst):
    tempSum  = 0
    for x in lst:
        tempSum += x
    return tempSum / len(lst)

input_list = [1.9 , 2.5, 3.7, 2, 1.5, 6, 3, 4, 5, 2]
m = mean(input_list)
print(m)
print(deviation(input_list,m))