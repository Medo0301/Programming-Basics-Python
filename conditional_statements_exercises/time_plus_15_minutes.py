FIFTEEN_MINUTES = 15

hours = int(input())
minutes = int(input())

if minutes + FIFTEEN_MINUTES >= 60:
    hours += 1
    minutes = minutes + FIFTEEN_MINUTES - 60
else:
    minutes = minutes + FIFTEEN_MINUTES

if hours == 24:
    hours = 0

print(f"{hours}:{minutes:02d}")