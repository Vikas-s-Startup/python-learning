def main():
    user_input = 10
    sum = 0
    isTriangular = False
    for i in range(1, user_input + 1):
        sum += i
        if sum == user_input:
            isTriangular = True
            break

    if isTriangular:
        print(f"{user_input} is a triangular number")
    else:
        print(f"{user_input} is not a triangular number")

main()