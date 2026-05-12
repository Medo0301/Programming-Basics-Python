strawberries_price = float(input())
bananas_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price / 2
orange_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

total_sum = strawberries_kg * strawberries_price \
            + raspberries_kg * raspberries_price \
            + bananas_kg * bananas_price \
            + orange_kg * orange_price

print(f"{total_sum:.2f}")