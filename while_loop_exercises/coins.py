COIN_200 = 200
COIN_100 = 100
COIN_50 = 50
COIN_20 = 20
COIN_10 = 10
COIN_5 = 5
COIN_2 = 2
COIN_1 = 1

change = float(input())
change = round(change * 100)
coins = 0

while change > 0:
    if change - COIN_200 >= 0:
        change -= COIN_200

    elif change - COIN_100 >= 0:
        change -= COIN_100

    elif change - COIN_50 >= 0:
        change -= COIN_50

    elif change - COIN_20 >= 0:
        change -= COIN_20

    elif change - COIN_10 >= 0:
        change -= COIN_10

    elif change - COIN_5 >= 0:
        change -= COIN_5

    elif change - COIN_2 >= 0:
        change -= COIN_2

    elif change - COIN_1 >= 0:
        change -= COIN_1

    coins += 1

print(coins)

# if change // COIN_200 != 0:
#     coins += change // COIN_200
#     change = change % COIN_200
# if change // COIN_100 != 0:
#     coins += change // COIN_100
#     change = change % COIN_100
# if change // COIN_50 != 0:
#     coins += change // COIN_50
#     change = change % COIN_50
# if change // COIN_20 != 0:
#     coins += change // COIN_20
#     change = change % COIN_20
# if change // COIN_10 != 0:
#     coins += change // COIN_10
#     change = change % COIN_10
# if change // COIN_5 != 0:
#     coins += change // COIN_5
#     change = change % COIN_5
# if change // COIN_2 != 0:
#     coins += change // COIN_2
#     change = change % COIN_2
# if change // COIN_1 != 0:
#     coins += change // COIN_1
#     change = change % COIN_1
#
# print(int(coins))