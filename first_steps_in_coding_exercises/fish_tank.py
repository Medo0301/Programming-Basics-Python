length = int(input())
width = int(input())
height = int(input())
filled_percentage = float(input())

tank_volume = (length * width * height) / 1000
needed_liters = tank_volume * (1 - filled_percentage / 100)

print(needed_liters)