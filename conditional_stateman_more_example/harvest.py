from  math import floor, ceil

vineyard_area = int(input())
grapes_per_sqm = float(input())
wine_needed = int(input())
workers_count = int(input())

total_wine = (vineyard_area * grapes_per_sqm) * 0.40 / 2.5

if total_wine < wine_needed:
    print(f"It will be a tough winter! More {floor(wine_needed - total_wine)} liters wine needed.")
else:
    wine_left = total_wine - wine_needed
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_left / workers_count)} liters per person.")
