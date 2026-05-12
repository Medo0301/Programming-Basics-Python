ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

days = int(input())
hotel_room = input()
rating = input()

total_price = 0

if hotel_room == "room for one person":
    total_price = (days - 1) * ROOM_FOR_ONE_PERSON

elif hotel_room == "apartment":
    total_price = (days - 1) * APARTMENT

    if days < 10:
        total_price -= total_price * 0.30
    elif 10 <= days <= 15:
        total_price -= total_price * 0.35
    elif days > 15:
        total_price -= total_price * 0.50

elif hotel_room == "president apartment":
    total_price = (days - 1) * PRESIDENT_APARTMENT

    if days < 10:
        total_price -= total_price * 0.10
    elif 10 <= days <= 15:
        total_price -= total_price * 0.15
    elif days > 15:
        total_price -= total_price * 0.20

if rating == "positive":
    total_price += total_price * 0.25
else:
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")