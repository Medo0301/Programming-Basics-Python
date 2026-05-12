ONE_MINUTE = 60

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third
minutes = total_time // ONE_MINUTE
seconds = total_time % ONE_MINUTE

print(f"{minutes}:{seconds:02d}") if seconds < 10 else print(f"{minutes}:{seconds}")