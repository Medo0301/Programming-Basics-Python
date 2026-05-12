MINIBUS_PRICE_PER_TON = 200
TRUCK_PRICE_PER_TON = 175
TRAIN_PRICE_PER_TON = 120

total_tons = 0
average_price_per_ton = 0
minibus_percentage = 0
truck_percentage = 0
train_percentage = 0

cargo_count = int(input())

for _ in range(cargo_count):
    cargo_weight = int(input())
    if cargo_weight <= 3:
        minibus_percentage += cargo_weight
    elif cargo_weight <= 11:
        truck_percentage += cargo_weight
    else:
        train_percentage += cargo_weight

total_tons = minibus_percentage + truck_percentage + train_percentage
average_price_per_ton = (minibus_percentage * MINIBUS_PRICE_PER_TON
                         + truck_percentage * TRUCK_PRICE_PER_TON
                         + train_percentage * TRAIN_PRICE_PER_TON) / total_tons
print(f"{average_price_per_ton:.2f}")
print(f"{(minibus_percentage / total_tons) * 100:.2f}%")
print(f"{(truck_percentage / total_tons) * 100:.2f}%")
print(f"{(train_percentage / total_tons) * 100:.2f}%")

