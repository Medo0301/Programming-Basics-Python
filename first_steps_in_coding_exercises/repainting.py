PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINNER = 5.00
BAGS_PRICE = 0.40

nylon_needed = int(input())
paint_needed = int(input())
paint_thinner = int(input())
work_hours = int(input())

total_nylon = (nylon_needed + 2) * PRICE_NYLON
total_paint = (paint_needed + (paint_needed * 0.10)) * PRICE_PAINT
total_thinner = paint_thinner * PRICE_THINNER
materials_cost = total_nylon + total_paint + total_thinner + BAGS_PRICE
total_workers_payment = (materials_cost * 0.30) * work_hours

final_price = materials_cost + total_workers_payment

print(final_price)