num = int(input())
count = 0
is_end = False

for row in range(1, num + 1):
    for col in range(1, row + 1):
        count += 1
        print(count, end=" ")

        if count == num:
            is_end = True
            break

    print()
    if is_end:
        break