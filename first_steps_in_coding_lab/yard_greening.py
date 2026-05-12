square_meters = float(input())

discount = square_meters * 7.61 * 0.18
final_price = square_meters * 7.61 - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")

