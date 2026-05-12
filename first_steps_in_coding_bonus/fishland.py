MUSSELS_PRICE_PER_KG = 7.50

mackerel_price_per_kg = float(input())
sprat_price_per_kg = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

bonito_total_price = (mackerel_price_per_kg + mackerel_price_per_kg * 0.60) \
                     * bonito_kg
horse_mackerel_total_price = (sprat_price_per_kg + sprat_price_per_kg * 0.80) \
                             * horse_mackerel_kg
mussels_total_price = mussels_kg * MUSSELS_PRICE_PER_KG

total = bonito_total_price + horse_mackerel_total_price + mussels_total_price

print(f"{total:.2f}")