WINTER_GROUP_PRICE_PER_NIGHT = 9.60
WINTER_MIXED_GROUP_PRICE_PER_NIGHT = 10

SPRING_GROUP_PRICE_PER_NIGHT = 7.20
SPRING_MIXED_GROUP_PRICE_PER_NIGHT = 9.50

SUMMER_GROUP_PRICE_PER_NIGHT = 15
SUMMER_MIXED_GROUP_PRICE_PER_NIGHT = 20

season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())
sport = ""
price = 0

if season == "Winter":

    if group_type == "boys":
        price = WINTER_GROUP_PRICE_PER_NIGHT
        sport = "Judo"
    elif group_type == "girls":
        price = WINTER_GROUP_PRICE_PER_NIGHT
        sport = "Gymnastics"
    elif group_type == "mixed":
        price = WINTER_MIXED_GROUP_PRICE_PER_NIGHT
        sport = "Ski"

elif season == "Spring":

    if group_type == "boys":
        price = SPRING_GROUP_PRICE_PER_NIGHT
        sport = "Tennis"
    elif group_type == "girls":
        price = SPRING_GROUP_PRICE_PER_NIGHT
        sport = "Athletics"
    elif group_type == "mixed":
        price = SPRING_MIXED_GROUP_PRICE_PER_NIGHT
        sport = "Cycling"

elif season == "Summer":

    if group_type == "boys":
        price = SUMMER_GROUP_PRICE_PER_NIGHT
        sport = "Football"
    elif group_type == "girls":
        price = SUMMER_GROUP_PRICE_PER_NIGHT
        sport = "Volleyball"
    elif group_type == "mixed":
        price = SUMMER_MIXED_GROUP_PRICE_PER_NIGHT
        sport = "Swimming"

price = price * nights_count * students_count

if 10 <= students_count < 20:
    price -= price * 0.05
elif 20 <= students_count < 50:
    price -= price * 0.15
elif students_count >= 50:
    price -= price * 0.50

print(f"{sport} {price:.2f} lv.")

