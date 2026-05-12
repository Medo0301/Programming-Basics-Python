POINTS_50 = 50
POINTS_100 = 100
PERCENTAGE_40 = 0.40
PERCENTAGE_30 = 0.30
PERCENTAGE_20 = 0.20

total_moves = int(input())
result = 0.0

from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for _ in range(total_moves):
    number = int(input())
    if 0 <= number <= 9:
        from_0_to_9 += 1
        result += number * PERCENTAGE_20
    elif 10 <= number <= 19:
        from_10_to_19 += 1
        result += number * PERCENTAGE_30
    elif 20 <= number <= 29:
        from_20_to_29 += 1
        result += number * PERCENTAGE_40
    elif 30 <= number <= 39:
        from_30_to_39 += 1
        result += POINTS_50
    elif 40 <= number <= 50:
        from_40_to_50 += 1
        result += POINTS_100
    else:
        invalid_numbers += 1
        result /= 2

print(f"{result:.2f}")
print(f"From 0 to 9: {from_0_to_9 / total_moves * 100:.2f}%")
print(f"From 10 to 19: {from_10_to_19 / total_moves * 100:.2f}%")
print(f"From 20 to 29: {from_20_to_29 / total_moves * 100:.2f}%")
print(f"From 30 to 39: {from_30_to_39 / total_moves * 100:.2f}%")
print(f"From 40 to 50: {from_40_to_50 / total_moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / total_moves * 100:.2f}%")
