PLAY_TIME_FOR_YEAR = 30000
DAY_OFF_PLAY_TIME = 127
WORK_DAY_PLAY_TIME = 63
DAYS_OF_YEAR =365

days_off = int(input())

days_off_play_time = days_off * DAY_OFF_PLAY_TIME
work_days_play_time = (DAYS_OF_YEAR - days_off) * WORK_DAY_PLAY_TIME
total_play_time = days_off_play_time + work_days_play_time

if total_play_time > PLAY_TIME_FOR_YEAR:
    hours_more = (total_play_time - PLAY_TIME_FOR_YEAR) // 60
    minutes_more = (total_play_time - PLAY_TIME_FOR_YEAR) % 60
    print("Tom will run away")
    print(f"{hours_more} hours and {minutes_more} minutes more for play")
else:
    hours_left = (PLAY_TIME_FOR_YEAR - total_play_time) // 60
    minutes_left = (PLAY_TIME_FOR_YEAR - total_play_time) % 60
    print("Tom sleeps well")
    print(f"{hours_left} hours and {minutes_left} minutes less for play")
