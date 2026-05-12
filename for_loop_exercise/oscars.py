MIN_NOMINATION_POINTS = 1250.5

actor_name = input()
point_from_academi = float(input())
judges_count = int(input())

for n in range(judges_count):
    judge_name = input()
    judge_points = float(input())

    point_from_academi += (len(judge_name) * judge_points) / 2

    if point_from_academi > MIN_NOMINATION_POINTS:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {point_from_academi:.1f}!")
        break

if point_from_academi <= MIN_NOMINATION_POINTS:
    print(f"Sorry, {actor_name} you need {MIN_NOMINATION_POINTS - point_from_academi:.1f} more!")