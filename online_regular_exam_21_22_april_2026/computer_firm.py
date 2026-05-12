computers_count = int(input())
count_sales = 0
avg_rating = 0

for _ in range(computers_count):
    sales_and_rating_data = int(input())
    rating = sales_and_rating_data % 10
    possible_sales = sales_and_rating_data // 10
    avg_rating += rating

    if rating == 3:
        count_sales += possible_sales * 0.5
    elif rating == 4:
        count_sales += possible_sales * 0.7
    elif rating == 5:
        count_sales += possible_sales * 0.85
    elif rating == 6:
        count_sales += possible_sales

print(f"{count_sales:.2f}")
print(f"{avg_rating / computers_count:.2f}")
