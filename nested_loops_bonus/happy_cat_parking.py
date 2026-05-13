TAX_EVEN_DAY_ODD_HOUR = 2.50
TAX_ODD_DAY_EVEN_HOUR = 1.25
STANDARD_TAX = 1.00

number_of_days = int(input())
number_of_hours_for_day = int(input())

total_sum = 0

for day in range(1, number_of_days + 1):
    sum_for_day = 0
    for hour in range(1, number_of_hours_for_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            sum_for_day += TAX_EVEN_DAY_ODD_HOUR
        elif day % 2 != 0 and hour % 2 == 0:
            sum_for_day += TAX_ODD_DAY_EVEN_HOUR
        else:
            sum_for_day += STANDARD_TAX

    print(f"Day: {day} - {sum_for_day:.2f} leva")
    total_sum += sum_for_day

print(f"Total: {total_sum:.2f} leva")
