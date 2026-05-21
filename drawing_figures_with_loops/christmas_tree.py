num = int(input())
char = "*"

for row in range(num + 1):
    for col_1 in range(num - row):
        print(" ", end="")
    print(char * row, end="")
    print(" | ", end="")
    for col_2 in range(row):
        print(char, end="")
    print()