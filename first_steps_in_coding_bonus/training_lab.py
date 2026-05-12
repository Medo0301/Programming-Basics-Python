DESK_W = 120
DESK_H = 70
CORIDOR_H = 100

w = float(input()) * 100
h = float(input()) * 100

rows = w // 120
desk_per_row = (h - 100) // 70

total_desks = rows * desk_per_row - 3
print(total_desks)