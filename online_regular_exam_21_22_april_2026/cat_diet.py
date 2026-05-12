CALORIES_PER_GRAM_FAT = 9
CALORIES_PER_GRAM_PROTEIN = 4
CALORIES_PER_GRAM_CARBOHYDRATE = 4

fat_percentage = int(input()) / 100
protein_percentage = int(input()) / 100
carbohydrate_percentage = int(input()) / 100
total_calories = int(input())
water_content_percentage = int(input()) / 100

total_gram_fat = total_calories * fat_percentage / CALORIES_PER_GRAM_FAT
total_gram_protein = total_calories * protein_percentage / CALORIES_PER_GRAM_PROTEIN
total_gram_carbohydrate = total_calories * carbohydrate_percentage / CALORIES_PER_GRAM_CARBOHYDRATE

food_grams = total_gram_fat + total_gram_protein + total_gram_carbohydrate

calories_per_gram = total_calories / food_grams
calories_per_gram -= calories_per_gram * water_content_percentage

print(f"{calories_per_gram:.4f}")
