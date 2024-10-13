
# quotient = int(input("Enter a decimal Integer"))
quotient = 343123298
binary = ""


while quotient !=0:
    rem = quotient % 2
    quotient = quotient // 2
    binary += str(rem)

print(binary)