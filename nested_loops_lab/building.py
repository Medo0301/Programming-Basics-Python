number_of_floors = int(input())
rooms_on_the_floor = int(input())

for floor in range(number_of_floors, 0, -1):
    for room in range(rooms_on_the_floor):
        if floor == number_of_floors:
            print(f"L{floor}{room}", end=" ")
        elif floor % 2 != 0:
            print(f"A{floor}{room}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=" ")

    print()
