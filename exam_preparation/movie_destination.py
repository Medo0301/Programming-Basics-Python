DUBAI_WINTER_PRICE = 45000
DUBAI_SUMMER_PRICE = 40000
SOFIA_WINTER_PRICE = 17000
SOFIA_SUMMER_PRICE = 12500
LONDON_WINTER_PRICE = 24000
LONDON_SUMMER_PRICE = 20250
DUBAI_DISCOUNT = 0.30
SOFIA_TAX_INCREASE = 0.25

budget = float(input())
destination = input()
season = input()
count_days = int(input())

total_sum = 0

if destination == "Dubai":
    if season == "Winter":
        total_sum = count_days * (DUBAI_WINTER_PRICE - DUBAI_WINTER_PRICE * DUBAI_DISCOUNT)
    elif season == "Summer":
        total_sum = count_days * (DUBAI_SUMMER_PRICE - DUBAI_SUMMER_PRICE * DUBAI_DISCOUNT)

elif destination == "Sofia":
    if season == "Winter":
        total_sum = count_days * (SOFIA_WINTER_PRICE + SOFIA_WINTER_PRICE * SOFIA_TAX_INCREASE)
    elif season == "Summer":
        total_sum = count_days * (SOFIA_SUMMER_PRICE + SOFIA_SUMMER_PRICE * SOFIA_TAX_INCREASE)

elif destination == "London":
    if season == "Winter":
        total_sum = count_days * LONDON_WINTER_PRICE
    elif season == "Summer":
        total_sum = count_days * LONDON_SUMMER_PRICE

if budget >= total_sum:
    print(f"The budget for the movie is enough! We have {budget - total_sum:.2f} leva left!")
else:
    print(f"The director needs {total_sum - budget:.2f} leva more!")