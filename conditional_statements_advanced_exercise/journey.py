# BULGARIA = "Bulgaria"
# BALKANS = "Balkans"
# EUROPE = "Europe"
# CAMP = "Camp"
# HOTEL = "Hotel"
# SUMMER = "summer"
# WINTER = "winter"

budget = float(input())
season = input()
destination = ""
vacation_type = ""
spent_amount = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_type = "Camp"
        spent_amount = budget * 0.30
    elif season == "winter":
        vacation_type = "Hotel"
        spent_amount = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_type = "Camp"
        spent_amount = budget * 0.40
    elif season == "winter":
        vacation_type = "Hotel"
        spent_amount = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    spent_amount = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {spent_amount:.2f}")