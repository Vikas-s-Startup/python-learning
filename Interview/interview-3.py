N = 1041

binary_rep = bin(N)[2:]
print(binary_rep)

# Split the binary representation by '1' to find sequences of '0's
gaps = binary_rep.strip('0')
print(gaps)
gaps = gaps.split('1')
print(gaps)

test =  map(len, gaps)

print(test)


print(type(test))
final = max(test)

print(final)

