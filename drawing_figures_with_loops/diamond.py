num = int(input())

star = "*"
line = "-"


if num % 2 == 0:
    start_star = 2
    left_right_line = num // 2 - 1
    middle_line = 2
    rng = num - 1
else:
    start_star = 1
    left_right_line = num // 2
    middle_line = 1
    rng = num

for row in range(rng):
    if row == 0 or row == rng - 1:
        print(line * left_right_line, end="")
        print(star * start_star, end="")
        print(line * left_right_line, end="")
        print()
        left_right_line -= 1
    else:
        print(line * left_right_line, end="")
        print(star, end="")
        print(line * middle_line, end="")
        print(star, end="")
        print(line * left_right_line, end="")
        print()

        if row < rng // 2:
            left_right_line -= 1
            middle_line += 2
        else:
            left_right_line += 1
            middle_line -= 2
