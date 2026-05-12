PENS_PACK_PRICE = 5.80
MARKERS_PACK_PRICE = 7.20
CLEANER_PRICE = 1.20

number_of_pens = int(input())
number_of_markers = int(input())
cleaner_l = int(input())
discount = int(input()) / 100

total = (number_of_pens * PENS_PACK_PRICE
         + number_of_markers * MARKERS_PACK_PRICE
         + cleaner_l * CLEANER_PRICE)

total -= (total * discount)

print(total)