import math

tennis_rocket_price = float(input())
tennis_rocket_count = int(input())
sneakers_pairs = int(input())

sneakers_price = tennis_rocket_price / 6
total_price = tennis_rocket_price * tennis_rocket_count \
              + sneakers_price * sneakers_pairs
total_price += total_price * 0.2


print(f"Price to be paid by Djokovic {math.floor(total_price / 8)}")
print(f"Price to be paid by sponsors {math.ceil(total_price / 8 * 7)}")
