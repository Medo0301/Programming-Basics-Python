from math import ceil, floor

MAGNOLIA_PRICE = 3.25
HYACINTH_PRICE = 4
ROSE_PRICE = 3.5
CACTUS_PRICE = 8

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())

total_earn = magnolia_count * MAGNOLIA_PRICE \
             + hyacinth_count * HYACINTH_PRICE \
             + rose_count * ROSE_PRICE \
             + cactus_count * CACTUS_PRICE
total_earn -= total_earn * 0.05

if total_earn >= gift_price:
    print(f"She is left with {floor(total_earn - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(gift_price - total_earn)} leva.")
