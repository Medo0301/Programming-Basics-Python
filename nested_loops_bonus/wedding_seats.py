last_sector = input()
rows = int(input())
seat_number_in_odd_row = int(input())
total_seats = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, rows + 1):
        seat = ord('a')
        if row % 2 != 0:
            for _ in range(seat_number_in_odd_row):
                print(f"{chr(sector)}{row}{chr(seat)}")
                seat += 1
                total_seats += 1
        else:
            for _ in range(seat_number_in_odd_row + 2):
                print(f"{chr(sector)}{row}{chr(seat)}")
                seat += 1
                total_seats += 1

    rows += 1

print(total_seats)
