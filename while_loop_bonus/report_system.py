MAX_CASH_PRICE = 100
MIN_CARD_PRICE = 10

needed_amount = int(input())
cash_sum = 0
card_sum = 0
cash_payment_count = 0
card_payment_count = 0
transaction_count = 0
total_sum = 0

while total_sum < needed_amount:
    command = input()

    if command == "End":
        break

    product_price = int(command)
    transaction_count += 1

    if transaction_count % 2 != 0:
        if product_price > MAX_CASH_PRICE:
            print("Error in transaction!")
            continue
        else:
            print("Product sold!")
            cash_sum += product_price
            cash_payment_count += 1
    else:
        if product_price < MIN_CARD_PRICE:
            print("Error in transaction!")
            continue
        else:
            print("Product sold!")
            card_sum += product_price
            card_payment_count += 1

    total_sum += product_price

if total_sum >= needed_amount:
    print(f"Average CS: {cash_sum / cash_payment_count:.2f}")
    print(f"Average CC: {card_sum / card_payment_count:.2f}")
else:
    print("Failed to collect required money for charity.")
