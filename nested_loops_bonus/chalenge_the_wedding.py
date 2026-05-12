men = int(input())
women = int(input())
max_number_of_table = int(input())
is_full = False

for man in range(1, men + 1):
    if is_full:
        break
    for woman in range(1, women + 1):
        print(f"({man} <-> {woman})", end=" ")
        max_number_of_table -= 1
        if max_number_of_table == 0:
            is_full = True
            break
