num = int(input())

for row in range(1, num + 1):
    if row == 1 or row == num:
        for col in range(num * 5):
            if col < num * 2 or col >= num * 3:
                print("*", end="")
            else:
                print(" ", end="")

    else:
        for col in range(1, num * 5 + 1):
            if col == 1 or col == num * 2 \
                    or col == num * 3 + 1 or col == num * 5:
                print("*", end="")

            elif (1 < col < num * 2) \
                    or (num * 3 + 1 < col < num * 5):
                print("/", end="")

            elif row == (num + 1) // 2:
                print("|", end="")

            else:
                print(" ", end="")

    print()


