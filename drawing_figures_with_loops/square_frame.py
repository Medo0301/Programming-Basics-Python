num = int(input())

for row in range(num):
    for col in range(num):
        if (row == 0 or row == num - 1) and\
                (col == 0 or col == num - 1):
            print("+", end=" ")
        elif col != 0 and col != num - 1:
            print("-", end=" ")
        else:
            print("|", end=" ")

    print()