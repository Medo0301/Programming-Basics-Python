COIN_1_LV = 1
COIN_2_LV = 2
BANKNOTE_5_LV = 5

coins_1_lv = int(input())
coins_2_lv = int(input())
banknotes_5_lv = int(input())
sum = int(input())

for coin_1 in range(coins_1_lv + 1):
    for coin_2 in range(coins_2_lv + 1):
        for banknote_5 in range(banknotes_5_lv + 1):
            if coin_1 * COIN_1_LV + coin_2 * COIN_2_LV + banknote_5 * BANKNOTE_5_LV == sum:
                print(f"{coin_1} * 1 lv. + {coin_2} * 2 lv. + {banknote_5} * 5 lv. = {sum} lv.")

