ECONOMY_CLASS_RENT = 100
COMPACT_CLASS_RENT = 500

budget = float(input())
season = input()
car_class = ""
car = ""
price = 0

if budget <= ECONOMY_CLASS_RENT:
    car_class = "Economy class"

    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    else:
        car = "Jeep"
        price = budget * 0.65

elif ECONOMY_CLASS_RENT < budget <= COMPACT_CLASS_RENT:
    car_class = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    else:
        car = "Jeep"
        price = budget * 0.80
else:
    car_class = "Luxury class"
    car = "Jeep"
    price = budget * 0.90

print(car_class)
print(f"{car} - {price:.2f}")