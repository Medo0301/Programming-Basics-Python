num = int(input())
string_for_print = "* "

for row in range(1, num + 1):
    for col in range(num - row):
        print(" ", end="")
    print(string_for_print * row)

for row in range(num, 1, -1):
    for col in range(num - row + 1):
        print(" ", end="")
    print(string_for_print * (row - 1))