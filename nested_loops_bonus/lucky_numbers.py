number = int(input())

for num in range(1111, 10000):
    num_to_str = str(num)
    if '0' in num_to_str:
        continue

    left_two_digit_sum = 0
    right_two_digit_sum = 0
    for index, digit in enumerate(num_to_str):
        if index < (len(num_to_str) // 2):
            left_two_digit_sum += int(digit)
        else:
            right_two_digit_sum += int(digit)

    if left_two_digit_sum == right_two_digit_sum and number % left_two_digit_sum == 0:
        print(num, end=" ")
