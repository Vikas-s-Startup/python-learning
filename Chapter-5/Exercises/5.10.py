CHEAPEST_AIRLINE = ""
CHEAPEST_PRICE = int(0)
CURRENT_CHEAPEST_AIRLINE = ""
CURRENT_CHEAPEST_PRICE = int(0)
current_airline = 0

airlines_input = input("Enter the number of airlines: ")

while int(current_airline) < int(airlines_input):
    airline_name = input("Enter an airline Name: ")
    airline_price = input("Enter ticket price: ")

    CURRENT_CHEAPEST_AIRLINE = airline_name
    CURRENT_CHEAPEST_PRICE = airline_price

    if int(CHEAPEST_PRICE) != 0:
        if CURRENT_CHEAPEST_PRICE < CHEAPEST_PRICE:
            CHEAPEST_PRICE = CURRENT_CHEAPEST_PRICE
            CHEAPEST_AIRLINE = CURRENT_CHEAPEST_AIRLINE
    else:
        CHEAPEST_PRICE = CURRENT_CHEAPEST_PRICE
        CHEAPEST_AIRLINE = CURRENT_CHEAPEST_AIRLINE

    current_airline += 1

print(f"CHEAPEST AIRLINE NAME: {CHEAPEST_AIRLINE} and the cheapest ticket of all is {CHEAPEST_PRICE}")