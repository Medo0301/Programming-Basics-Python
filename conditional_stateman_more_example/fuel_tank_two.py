DIESEL = 2.33
GASOLINE = 2.22
GAS = 0.93
DISCOUNT_DIESEL = 0.12
DISCOUNT_GASOLINE = 0.18
DISCOUNT_GAS = 0.08

type_of_fuel = input()
liters_fuel = float(input())
card = input()

total = 0

if card == "Yes":
    if type_of_fuel == "Gasoline":
        total = (GASOLINE - DISCOUNT_GASOLINE) * liters_fuel
    elif type_of_fuel == "Diesel":
        total = (DIESEL - DISCOUNT_DIESEL) * liters_fuel
    elif type_of_fuel == "Gas":
        total = (GAS - DISCOUNT_GAS) * liters_fuel
elif card == "No":
    if type_of_fuel == "Gasoline":
        total = GASOLINE * liters_fuel
    elif type_of_fuel == "Diesel":
        total = DIESEL * liters_fuel
    elif type_of_fuel == "Gas":
        total = GAS * liters_fuel

if 20 <= liters_fuel <= 25:
    total -= total * 0.08
elif liters_fuel > 25:
    total -= total * 0.10

print(f"{total:.2f} lv.")