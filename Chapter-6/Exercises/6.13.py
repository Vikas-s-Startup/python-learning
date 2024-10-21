def calculateSumSeries(i):
    sum_series = 0
    while i != 0:
        sum_series += i / (i + 1)
        i -= 1
    return sum_series

def main():
    print("i", "            ", "m(i)")
    for i in range(1, 21):
        print(i,"            ", calculateSumSeries(i))

main()