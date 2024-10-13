FEE_INCREASE_PER_YEAR = 1.05

TOTAL_FEE = 10000
year = 0

for year in range(0, 11):
    TOTAL_FEE =+ TOTAL_FEE * FEE_INCREASE_PER_YEAR
    # while
    print(f"YEAR {year}: FEE {str(format(TOTAL_FEE, ".2f"))}")

print(f" \nFEE AFTER 10 years is {str(format(TOTAL_FEE, ".2f"))} \n")

LAST_4_YEAR_FEE = TOTAL_FEE
for year in range(10, 15):
    LAST_4_YEAR_FEE = + LAST_4_YEAR_FEE * FEE_INCREASE_PER_YEAR
    print(f"YEAR {year}: FEE {str(format(LAST_4_YEAR_FEE, ".2f"))}")
