while True:
    destination = input()

    if destination == "End":
        break

    budget = float(input())
    amount = 0
    while True:
        sum = float(input())
        amount += sum

        if amount >= budget:
            print(f"Going to {destination}!")
            break

