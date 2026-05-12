number = int(input())

first_range = number % 10
number = number // 10
second_range = number % 10
number = number // 10
third_range = number % 10

for digit_1 in range(1, first_range + 1):
    for digit_2 in range(1, second_range + 1):
        for digit_3 in range(1, third_range + 1):
            print(f"{digit_1} * {digit_2} * {digit_3} = {digit_1 * digit_2 * digit_3};")

