GOAL_STEPS = 10000
steps_for_the_day = 0

while steps_for_the_day < GOAL_STEPS:
    comand = input()

    if comand == "Going home":
        steps = int(input())
        steps_for_the_day += steps
        break

    steps_for_the_day += int(comand)

if steps_for_the_day > GOAL_STEPS:
    print("Goal reached! Good job!")
    print(f"{abs(steps_for_the_day - GOAL_STEPS)} steps over the goal!")
else:
    print(f"{abs(steps_for_the_day - GOAL_STEPS)} more steps to reach goal.")

