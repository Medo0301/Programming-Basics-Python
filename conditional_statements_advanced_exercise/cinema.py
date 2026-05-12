PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

projection_type = input()
rows = int(input())
columns = int(input())
income = 0
cinema_capacity = rows * columns

if projection_type == "Premiere":
    income = cinema_capacity * PREMIERE
elif projection_type == "Normal":
    income = cinema_capacity * NORMAL
elif projection_type == "Discount":
    income = cinema_capacity * DISCOUNT

print(f"{income:.2f} leva")
