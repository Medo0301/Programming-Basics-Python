tipe_of_fuel = input().lower()
liters_fuel = int(input())

if liters_fuel >= 25:
    if tipe_of_fuel == "diesel":
        print(f"You have enough {tipe_of_fuel}.")
    elif tipe_of_fuel == "gasoline":
        print(f"You have enough {tipe_of_fuel}.")
    elif tipe_of_fuel == "gas":
        print(f"You have enough {tipe_of_fuel}.")
    else:
        print("Invalid fuel!")
else:
    if tipe_of_fuel == "diesel":
        print(f"Fill your tank with {tipe_of_fuel}!")
    elif tipe_of_fuel == "gasoline":
        print(f"Fill your tank with {tipe_of_fuel}!")
    elif tipe_of_fuel == "gas":
        print(f"Fill your tank with {tipe_of_fuel}!")
    else:
        print("Invalid fuel!")