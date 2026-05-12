DISCOUNT = 0.05

budget = float(input())
count_nights = int(input())
nights_price = float(input())
extra_expenses_pct = int(input())

if count_nights > 7:
    nights_price -= nights_price * DISCOUNT

total_sum = (nights_price * count_nights) + (budget * extra_expenses_pct / 100)

if total_sum <= budget:
    print(f"Ivanovi will be left with {budget - total_sum:.2f} leva after vacation.")
else:
    print(f"{total_sum - budget:.2f} leva needed.")