number = int(input())
sum = 0

for _ in range(number):
    next_number = int(input())

    sum += next_number

print(f"{sum / number:.2f}")