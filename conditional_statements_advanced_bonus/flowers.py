CHRYSANTHEMUMS_SPRING_SUMMER_PRICE = 2.00
CHRYSANTHEMUMS_AUTUMN_WINTER_PRICE = 3.75
ROSES_SPRING_SUMMER_PRICE = 4.10
ROSES_AUTUMN_WINTER_PRICE = 4.50
TULIPS_SPRING_SUMMER_PRICE = 2.50
TULIPS_AUTUMN_WINTER_PRICE = 4.15
ARRANGEMENT_COST = 2.00

chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()
total_price = 0

chrysanthemums_spring_summer_price = CHRYSANTHEMUMS_SPRING_SUMMER_PRICE
chrysanthemums_autumn_winter_price = CHRYSANTHEMUMS_AUTUMN_WINTER_PRICE
roses_spring_summer_price = ROSES_SPRING_SUMMER_PRICE
roses_autumn_winter_price = ROSES_AUTUMN_WINTER_PRICE
tulips_spring_summer_price = TULIPS_SPRING_SUMMER_PRICE
tulips_autumn_winter_price = TULIPS_AUTUMN_WINTER_PRICE

if is_holiday == "Y":
    chrysanthemums_spring_summer_price += chrysanthemums_spring_summer_price * 0.15
    chrysanthemums_autumn_winter_price += chrysanthemums_autumn_winter_price * 0.15
    roses_spring_summer_price += roses_spring_summer_price * 0.15
    roses_autumn_winter_price += roses_autumn_winter_price * 0.15
    tulips_spring_summer_price += tulips_spring_summer_price * 0.15
    tulips_autumn_winter_price += tulips_autumn_winter_price * 0.15


if season == "Spring" or season == "Summer":
    total_price = chrysanthemums_count * chrysanthemums_spring_summer_price \
                  + roses_count * roses_spring_summer_price \
                  + tulips_count * tulips_spring_summer_price
    if season == "Spring" and tulips_count > 7:
        total_price -= total_price * 0.05

elif season == "Autumn" or season == "Winter":
    total_price = chrysanthemums_count * chrysanthemums_autumn_winter_price \
                  + roses_count * roses_autumn_winter_price \
                  + tulips_count * tulips_autumn_winter_price
    if season == "Winter" and roses_count >= 10:
        total_price -= total_price * 0.10

if chrysanthemums_count + roses_count + tulips_count > 20:
    total_price -= total_price * 0.20

total_price += ARRANGEMENT_COST

print(f"{total_price:.2f}")
