from math import floor

WIN_POINTS = 2000
FINAL_POINTS = 1200
SEMI_FINAL_POINTS = 720

tournament_count = int(input())
start_points = int(input())
win = 0
average_point = 0

for _ in range(tournament_count):
    tournament_stage = input()

    if tournament_stage == "W":
        average_point += WIN_POINTS
        win += 1

    elif tournament_stage == "F":
        average_point += FINAL_POINTS

    elif tournament_stage == "SF":
        average_point += SEMI_FINAL_POINTS

print(f"Final points: {start_points + average_point}")
print(f"Average points: {floor(average_point / tournament_count)}")
print(f"{(win / tournament_count) * 100:.2f}%")

