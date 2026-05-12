from math import floor

record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

total_time = distance_meters * seconds_per_meter + \
             floor(distance_meters / 15) * 12.5

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_seconds:.2f} seconds slower.")
