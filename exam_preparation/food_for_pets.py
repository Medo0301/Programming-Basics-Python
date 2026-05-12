COOKIES_EATEN = 0.10

count_days = int(input())
food = float(input())

total_eaten_cookies = 0
total_eaten_food = 0
total_dog_eaten_food = 0
total_cat_eaten_food = 0


for day in range(1, count_days + 1):
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())

    if day % 3 == 0:
        total_eaten_cookies += (dog_food_eaten + cat_food_eaten) * COOKIES_EATEN

    total_dog_eaten_food += dog_food_eaten
    total_cat_eaten_food += cat_food_eaten

total_eaten_food = total_dog_eaten_food + total_cat_eaten_food

print(f"Total eaten biscuits: {round(total_eaten_cookies)}gr.")
print(f"{total_eaten_food / food * 100:.2f}% of the food has been eaten.")
print(f"{total_dog_eaten_food / total_eaten_food * 100:.2f}% eaten from the dog.")
print(f"{total_cat_eaten_food / total_eaten_food * 100:.2f}% eaten from the cat.")
