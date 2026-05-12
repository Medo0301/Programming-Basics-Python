from math import floor, ceil

days = int(input())
food_kg = int(input())
dog_food_for_day = float(input())
cat_food_for_day = float(input())
turtle_food_for_day = float(input())

dog_needed_food = dog_food_for_day * days
cat_needed_food = cat_food_for_day * days
turtle_needed_food = (turtle_food_for_day / 1000) * days
total_needed_food = dog_needed_food + cat_needed_food + turtle_needed_food

if total_needed_food <= food_kg:
    print(f"{floor(food_kg - total_needed_food)} kilos of food left.")
else:
    print(f"{ceil(total_needed_food - food_kg)} more kilos of food are needed.")