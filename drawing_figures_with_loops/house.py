num = int(input())

star = "*"
line = "-"

if num % 2 == 0:
    start_star = 2
    start_line = num // 2 - 1
else:
    start_star = 1
    start_line = num // 2

for row in range((num + 1) // 2):

    print(line * start_line, end="")
    print(star * start_star, end="")
    print(line * start_line, end="")
    print()

    start_line -= 1
    start_star += 2

for row in range(num // 2):
    for col in range(num):
        if col == 0 or col == num - 1:
            print("|", end="")
        else:
            print(star, end="")

    print()