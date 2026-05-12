SPENDING_PER_YEAR = 12000
STARTED_YEAR = 1800

heritage_money = float(input())
end_year = int(input())

age = 18
total_spend = 0

for year in range(STARTED_YEAR, end_year + 1):
    if year % 2 == 0:
        total_spend += SPENDING_PER_YEAR
    else:
        total_spend += SPENDING_PER_YEAR + 50 * age

    age += 1

if heritage_money >= total_spend:
    print(f"Yes! He will live a carefree life and will have {heritage_money - total_spend:.2f} dollars left.")
else:
    print(f"He will need {total_spend - heritage_money:.2f} dollars to survive.")