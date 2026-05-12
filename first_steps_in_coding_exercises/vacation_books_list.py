pages_in_book = int(input())
pages_for_hour = int(input())
days = int(input())

hours_per_day = (pages_in_book // pages_for_hour) // days

print(hours_per_day)