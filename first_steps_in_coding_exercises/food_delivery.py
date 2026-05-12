CHICKEN_MEAL_PRICE = 10.35
FISH_MEAL_PRICE = 12.40
VEGETARIAN_MEAL_PRICE = 8.15
DELIVERY_PRICE = 2.50
chicken_meals = int(input())
fish_meals = int(input())
vegetarian_meals = int(input())

total_price_for_meals = (chicken_meals * CHICKEN_MEAL_PRICE
                         + fish_meals * FISH_MEAL_PRICE
                         + vegetarian_meals * VEGETARIAN_MEAL_PRICE)
dessert_price = total_price_for_meals * 0.20

final_price = total_price_for_meals + dessert_price + DELIVERY_PRICE
print(final_price)
