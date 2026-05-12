month = input()
nights_count = int(input())
apartment_total_price = 0
studio_total_price = 0

if month == "May" or month == "October":
    apartment_total_price = nights_count * 65
    studio_total_price = nights_count * 50
    if 7 < nights_count <= 14:
        studio_total_price -= studio_total_price * 0.05
    elif nights_count > 14:
        studio_total_price -= studio_total_price * 0.30
elif month == "June" or month == "September":
    apartment_total_price = nights_count * 68.70
    studio_total_price = nights_count * 75.20
    if nights_count > 14:
        studio_total_price -= studio_total_price * 0.20
elif month == "July" or month == "August":
    apartment_total_price = nights_count * 77
    studio_total_price = nights_count * 76

if nights_count > 14:
    apartment_total_price -= apartment_total_price * 0.10

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")
