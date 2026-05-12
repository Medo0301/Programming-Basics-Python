WATER = 20
INTERNET = 15
PERCENTAGE_20 = 0.20

total_months = int(input())
total_electricity = 0
total_other_expenses = 0
total_bills = 0

for _ in range(total_months):
    electricity = float(input())
    total_electricity += electricity
    other_expenses = (electricity + WATER + INTERNET) \
                     + (electricity + WATER + INTERNET) * PERCENTAGE_20
    total_other_expenses += other_expenses
    total_bills += electricity + WATER + INTERNET + other_expenses

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {WATER * total_months:.2f} lv")
print(f"Internet: {INTERNET * total_months:.2f} lv")
print(f"Other: {total_other_expenses:.2f} lv")
print(f"Average: {total_bills / total_months:.2f} lv")