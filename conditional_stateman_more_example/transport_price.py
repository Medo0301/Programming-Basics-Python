kilometers = int(input())
time_of_day = input()
tariff = 0
total = 0

if time_of_day == "day":
    tariff = 0.79
else:
    tariff = 0.90

if kilometers < 20:
    total = tariff * kilometers + 0.70
elif 20 <= kilometers < 100:
    tariff = 0.09
    total = tariff * kilometers
else:
    tariff = 0.06
    total = tariff * kilometers

print(f"{total:.2f}")