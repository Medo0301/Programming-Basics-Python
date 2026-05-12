max_first_digit = int(input())
max_second_digit = int(input())
max_third_digit = int(input())

for digit_1 in range(2, max_first_digit + 1):
    if digit_1 % 2 == 0:
        for digit_2 in range(2, max_second_digit + 1):
            if digit_2 in [2, 3, 5, 7]:
                for digit_3 in range(2, max_third_digit + 1):
                    if digit_3 % 2 == 0:
                        print(digit_1, digit_2, digit_3)