FIRST_CHEAPEST_AIRLINE = ""
FIRST_CHEAPEST_PRICE = float('inf')  # Start with infinity as the largest possible price
SECOND_CHEAPEST_AIRLINE = ""
SECOND_CHEAPEST_PRICE = float('inf')
current_airline = 0

airlines_input = input("Enter the number of airlines (minimum 2): ")

while int(current_airline) < int(airlines_input):
    airline_name = input("Enter an airline Name: ")
    airline_price = float(input("Enter ticket price: "))

    if airline_price < FIRST_CHEAPEST_PRICE:
        # Shift the first cheapest to second cheapest
        SECOND_CHEAPEST_PRICE = FIRST_CHEAPEST_PRICE
        SECOND_CHEAPEST_AIRLINE = FIRST_CHEAPEST_AIRLINE
        # Update the first cheapest with current airline
        FIRST_CHEAPEST_PRICE = airline_price
        FIRST_CHEAPEST_AIRLINE = airline_name
    elif airline_price < SECOND_CHEAPEST_PRICE:
        # Update the second cheapest directly
        SECOND_CHEAPEST_PRICE = airline_price
        SECOND_CHEAPEST_AIRLINE = airline_name


    current_airline += 1

print(f"FIRST CHEAPEST AIRLINE NAME: {FIRST_CHEAPEST_AIRLINE} and the cheapest ticket of all is {FIRST_CHEAPEST_PRICE}")
print(f"SECOND CHEAPEST AIRLINE NAME: {SECOND_CHEAPEST_AIRLINE} and the SECOND cheapest ticket of all is {SECOND_CHEAPEST_PRICE}")
