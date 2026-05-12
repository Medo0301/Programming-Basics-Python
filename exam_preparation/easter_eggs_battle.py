first_player_eggs = int(input())
second_player_eggs = int(input())

is_end = False
while True:
    command = input()

    if command == "End":
        is_end = True
        break

    if command == "one":
        second_player_eggs -= 1
    elif command == "two":
        first_player_eggs -= 1

    if first_player_eggs <= 0 or second_player_eggs <= 0:
        break

if is_end:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")
elif first_player_eggs <= 0:
    print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
elif second_player_eggs <= 0:
    print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")