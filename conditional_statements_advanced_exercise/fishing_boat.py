SPRING_RENT = 3000
SUMMER_AUTUMN_RENT = 4200
WINTER_RENT = 2600

budget = int(input())
season = input()
fisherman_count = int(input())
total_price = 0

if season == "Spring":
    total_price = SPRING_RENT
elif season == "Summer" or season == "Autumn":
    total_price = SUMMER_AUTUMN_RENT
elif season == "Winter":
    total_price = WINTER_RENT

if fisherman_count <= 6:
    total_price -= total_price * 0.10
elif 7 <= fisherman_count <= 11:
    total_price -= total_price * 0.15
elif fisherman_count >= 12:
    total_price -= total_price * 0.25

if fisherman_count % 2 == 0 and season != "Autumn":
    total_price -= total_price * 0.05

if total_price <= budget:
    print(f"Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")
