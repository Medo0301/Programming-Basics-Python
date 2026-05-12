from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration / 8
time_for_rest = break_duration / 4
left_time = break_duration - time_for_lunch - time_for_rest

if left_time >= episode_duration:
    print(f"You have enough time to watch {series_name} "
          f"and left with {ceil(left_time - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, "
          f"you need {ceil(episode_duration - left_time)} more minutes.")
