needed_money = float(input())
balance = float(input())

number_of_days = 0
count_days_for_spend = 0
has_spend_5_days = False

while True:
    action = input()
    amount = float(input())

    number_of_days += 1

    if action == "spend":
        count_days_for_spend += 1
        balance -= amount
        if balance < 0:
            balance = 0

        if count_days_for_spend >= 5:
            has_spend_5_days = True
            break

    else:
        balance += amount
        count_days_for_spend = 0
        if balance >= needed_money:
            break


if has_spend_5_days:
    print("You can't save the money.")
    print(f"{number_of_days}")
else:
    print(f"You saved the money for {number_of_days} days.")