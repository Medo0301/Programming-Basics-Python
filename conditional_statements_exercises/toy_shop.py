travel_cost = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_sum = puzzles_count * 2.60 + dolls_count * 3 + \
            teddy_bears_count * 4.10 + minions_count * 8.20 +\
            trucks_count * 2

if puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count >= 50:
    total_sum -= total_sum * 0.25

total_sum -= total_sum * 0.1

if total_sum >= travel_cost:
    print(f"Yes! {(total_sum - travel_cost):.2f} lv left.")
else:
    print(f"Not enough money! {(travel_cost - total_sum):.2f} lv needed.")