movie_budget = float(input())
extras_count = int(input())
price_per_clothing = float(input())

decor_cost = movie_budget * 0.1
total_price_for_clothing = extras_count * price_per_clothing

if extras_count >= 150:
    total_price_for_clothing -= total_price_for_clothing * 0.1

movie_cost = decor_cost + total_price_for_clothing

if movie_budget >= movie_cost:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - movie_cost:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {movie_cost - movie_budget:.2f} leva more.")
