CAMP_BUDGET = 1000
HUT_BUDGET = 3000

budget = float(input())
season = input()

location = ""
accommodation_type = ""
price = 0

if budget <= CAMP_BUDGET:
    accommodation_type = "Camp"

    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45

elif CAMP_BUDGET < budget <= HUT_BUDGET:
    accommodation_type = "Hut"

    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    else:
        location = "Morocco"
        price = budget * 0.60

else:
    accommodation_type = "Hotel"
    price = budget * 0.90

    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {accommodation_type} - {price:.2f}")