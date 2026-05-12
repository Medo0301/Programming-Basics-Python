ages = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_count = 0
money = 0
total_money = 0

for age in range(1, ages + 1):
    if age % 2 != 0:
        toy_count += 1
    else:
        money += 10
        total_money += (money - 1)

total_money += toy_price * toy_count

if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money:.2f}")
