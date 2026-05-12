START = 1111
FINAL = 10000

number = int(input())


for idx in range(START, FINAL):
    idx_to_str = str(idx)
    is_special = True
    for digit in idx_to_str:
        if digit == '0' or number % int(digit) != 0:
            is_special = False
            break

    if is_special:
        print(idx, end=" ")