stadium_capacity = int(input())
total_fans = int(input())

fans_in_sector_A = 0
fans_in_sector_B = 0
fans_in_sector_V = 0
fans_in_sector_G = 0

for _ in range(total_fans):
    sector = input()
    if sector == "A":
        fans_in_sector_A += 1
    elif sector == "B":
        fans_in_sector_B += 1
    elif sector == "V":
        fans_in_sector_V += 1
    elif sector == "G":
        fans_in_sector_G += 1

print(f"{fans_in_sector_A / total_fans * 100:.2f}%")
print(f"{fans_in_sector_B / total_fans * 100:.2f}%")
print(f"{fans_in_sector_V / total_fans * 100:.2f}%")
print(f"{fans_in_sector_G / total_fans * 100:.2f}%")
print(f"{total_fans / stadium_capacity * 100:.2f}%")
