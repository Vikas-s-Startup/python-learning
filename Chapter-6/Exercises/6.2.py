def productOfDigits(n):
    product = 1
    for i in range(0,len(n)):
        if int(n[i]) != 0:
            product *= int(n[i])
    print(product)

productOfDigits("123405")

