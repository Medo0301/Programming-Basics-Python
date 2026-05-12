SPRING_PRICE_UP_TO_FIVE = 50.00
SPRING_PRICE_ABOVE_FIVE = 48.00
SUMMER_PRICE_UP_TO_FIVE = 48.50
SUMMER_PRICE_ABOVE_FIVE = 45.00
AUTUMN_PRICE_UP_TO_FIVE = 60.00
AUTUMN_PRICE_ABOVE_FIVE = 49.50
WINTER_PRICE_UP_TO_FIVE = 86.00
WINTER_PRICE_ABOVE_FIVE = 85.00

count_people = int(input())
season = input()
total_price = 0

if count_people <= 5:
    if season == "spring":
        total_price = count_people * SPRING_PRICE_UP_TO_FIVE
    elif season == "summer":
        total_price = count_people * SUMMER_PRICE_UP_TO_FIVE
        total_price -= total_price * 0.15
    elif season == "autumn":
        total_price = count_people * AUTUMN_PRICE_UP_TO_FIVE
    elif season == "winter":
        total_price = count_people * WINTER_PRICE_UP_TO_FIVE
        total_price += total_price * 0.08
else:
    if season == "spring":
        total_price = count_people * SPRING_PRICE_ABOVE_FIVE
    elif season == "summer":
        total_price = count_people * SUMMER_PRICE_ABOVE_FIVE
        total_price -= total_price * 0.15
    elif season == "autumn":
        total_price = count_people * AUTUMN_PRICE_ABOVE_FIVE
    elif season == "winter":
        total_price = count_people * WINTER_PRICE_ABOVE_FIVE
        total_price += total_price * 0.08

print(f"{total_price:.2f} leva.")