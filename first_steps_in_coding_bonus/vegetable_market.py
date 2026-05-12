BGN_TO_EURO_RATE = 1.94

price_for_vegetables = float(input())
price_for_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

sum_in_bgn = price_for_vegetables * kg_vegetables \
             + price_for_fruits * kg_fruits

total_in_euro = sum_in_bgn / BGN_TO_EURO_RATE

print(f"{total_in_euro:.2f}")