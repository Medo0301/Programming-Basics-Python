DOOR_AREA = 2.40
WINDOW_AREA = 2.25

x = float(input())
y = float(input())
h = float(input())

area_with_green_paint = (x * x - DOOR_AREA) + (x * x) \
                        + 2 * (x * y - WINDOW_AREA)
area_with_red_paint = 2 * (x * y) + 2 * ((x * h) / 2)

needed_green_paint = area_with_green_paint / 3.40
needed_red_paint = area_with_red_paint / 4.30

print(f"{needed_green_paint:.2f}")
print(f"{needed_red_paint:.2f}")