limit_hundreds = int(input())
limit_tens = int(input())
limit_units = int(input())

for digit_hundreds in range(2, limit_hundreds + 1, 2):
    for digit_tens in range(2, limit_tens + 1):
        if digit_tens in [2, 3, 5, 7]:
            for digit_units in range(2, limit_units + 1, 2):
                print(f"{digit_hundreds} {digit_tens} {digit_units}")
