ML_IN_BOTTLE = 750
ML_FOR_DISH = 5
ML_FOR_POT = 15

bottles = int(input())
detergent_ml = bottles * ML_IN_BOTTLE
clean_dishes = 0
clean_pots = 0
count_washing = 1

while detergent_ml >= 0:
    command = input()
    if command == "End":
        break

    vesseles_count = int(command)
    if count_washing % 3 != 0:
        detergent_ml -= ML_FOR_DISH * vesseles_count
        clean_dishes += vesseles_count
    else:
        detergent_ml -= ML_FOR_POT * vesseles_count
        clean_pots += vesseles_count

    count_washing += 1

if detergent_ml >= 0:
    print("Detergent was enough!")
    print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {detergent_ml} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_ml)} ml. more necessary!")