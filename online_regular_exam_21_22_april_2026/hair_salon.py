MENS_HAIRCUT = 15
LADIES_HAIRCUT = 20
KIDS_HAIRCUT = 10
COLOR_TOUCH_UP = 20
COLOR_FULL_COLOR = 30

daily_target = int(input())
revenue = 0

while revenue < daily_target:
    command = input()
    if command == "closed":
        break

    if command == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            revenue += MENS_HAIRCUT
        elif haircut_type == "ladies":
            revenue += LADIES_HAIRCUT
        elif haircut_type == "kids":
            revenue += KIDS_HAIRCUT
    elif command == "color":
        coloring_type = input()
        if coloring_type == "touch up":
            revenue += COLOR_TOUCH_UP
        elif coloring_type == "full color":
            revenue += COLOR_FULL_COLOR

if revenue >= daily_target:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {daily_target - revenue}lv. more.")

print(f"Earned money: {revenue}lv.")
