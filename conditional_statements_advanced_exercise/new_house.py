ROSE = 5
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

flower = input()
count_flower = int(input())
budget = int(input())
total_price = 0

if flower == "Roses":
    total_price = count_flower * ROSE
    if count_flower > 80:
        total_price -= total_price * 0.10
elif flower == "Dahlias":
    total_price = count_flower * DAHLIA
    if count_flower > 90:
        total_price -= total_price * 0.15
elif flower == "Tulips":
    total_price = count_flower * TULIP
    if count_flower > 80:
        total_price -= total_price * 0.15
elif flower == "Narcissus":
    total_price = count_flower * NARCISSUS
    if count_flower < 120:
        total_price += total_price * 0.15
elif flower == "Gladiolus":
    total_price = count_flower * GLADIOLUS
    if count_flower < 80:
        total_price += total_price * 0.20

if total_price <= budget:
    print(f"Hey, you have a great garden with {count_flower} {flower}"
          f" and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")