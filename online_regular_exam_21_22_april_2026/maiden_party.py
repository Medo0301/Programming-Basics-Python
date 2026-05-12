LOVE_MESSAGE_PRICE = 0.60
WAX_ROSE_PRICE = 7.20
KEYCHAIN_PRICE = 3.60
CARICATURE_PRICE = 18.20
LUCKY_SURPRISE_PRICE = 22

maiden_party_price = float(input())
count_love_message = int(input())
count_wax_rose = int(input())
count_keychain = int(input())
count_caricature = int(input())
count_lucky_surprise = int(input())

total_price = count_love_message * LOVE_MESSAGE_PRICE \
              + count_wax_rose * WAX_ROSE_PRICE \
              + count_keychain * KEYCHAIN_PRICE \
              + count_caricature * CARICATURE_PRICE \
              + count_lucky_surprise * LUCKY_SURPRISE_PRICE

total_items = count_love_message + count_wax_rose \
              + count_keychain + count_caricature \
              + count_lucky_surprise

if total_items >= 25:
    total_price -= total_price * 0.35

total_price -= total_price * 0.10

if total_price >= maiden_party_price:
    print(f"Yes! {total_price - maiden_party_price:.2f} lv left.")
else:
    print(f"Not enough money! {maiden_party_price - total_price:.2f} lv needed.")