SPRING_AUTUMN_RATE_TO_5000_KM = 0.75
SUMMER_RATE_TO_5000_KM = 0.90
WINTER_RATE_TO_5000_KM = 1.05

SPRING_AUTUMN_RATE_TO_10000_KM = 0.95
SUMMER_RATE_TO_10000_KM = 1.10
WINTER_RATE_TO_10000_KM = 1.25

RATE_TO_20000_KM = 1.45
TAX = 0.10
MONTHS_IN_SEASON = 4
KM_LIMIT_1 = 5000
KM_LIMIT_2 = 10000
KM_LIMIT_3 = 20000

season = input()
km_per_month = float(input())
salary = 0

if km_per_month <= KM_LIMIT_1:

    if season == "Spring" or season == "Autumn":
        salary = km_per_month * SPRING_AUTUMN_RATE_TO_5000_KM
    elif season == "Summer":
        salary = km_per_month * SUMMER_RATE_TO_5000_KM
    elif season == "Winter":
        salary = km_per_month * WINTER_RATE_TO_5000_KM

elif KM_LIMIT_1 < km_per_month <= KM_LIMIT_2:

    if season == "Spring" or season == "Autumn":
        salary = km_per_month * SPRING_AUTUMN_RATE_TO_10000_KM
    elif season == "Summer":
        salary = km_per_month * SUMMER_RATE_TO_10000_KM
    elif season == "Winter":
        salary = km_per_month * WINTER_RATE_TO_10000_KM

elif KM_LIMIT_2 < km_per_month <= KM_LIMIT_3:
    salary = km_per_month * RATE_TO_20000_KM

salary = salary * MONTHS_IN_SEASON
salary -= salary * TAX

print(f"{salary:.2f}")