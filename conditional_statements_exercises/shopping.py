PRICE_VIDEO_CARD = 250

budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

price_for_all_video_cards = video_cards_count * PRICE_VIDEO_CARD
price_per_processor = price_for_all_video_cards * 0.35
price_per_ram = price_for_all_video_cards * 0.10

total = price_for_all_video_cards + processors_count * price_per_processor\
        + ram_count * price_per_ram

if video_cards_count > processors_count:
    total -= total * 0.15

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")