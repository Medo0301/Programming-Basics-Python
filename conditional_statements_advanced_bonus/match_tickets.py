VIP_TICKET_PRICE = 499.99
NORMLA_TICKET_PRICE = 249.99

budget = float(input())
category = input()
number_of_people = int(input())

total_ticket_price = 0

if category == "VIP":
    total_ticket_price = number_of_people * VIP_TICKET_PRICE
elif category == "Normal":
    total_ticket_price = number_of_people * NORMLA_TICKET_PRICE

if 1 <= number_of_people <= 4:
    budget -= budget * 0.75
elif 5 <= number_of_people <= 9:
    budget -= budget * 0.60
elif 10 <= number_of_people <= 24:
    budget -= budget * 0.50
elif 25 <= number_of_people <= 49:
    budget -= budget * 0.40
elif number_of_people >= 50:
    budget -= budget * 0.25

if budget >= total_ticket_price:
    print(f"Yes! You have {budget - total_ticket_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_ticket_price - budget:.2f} leva.")