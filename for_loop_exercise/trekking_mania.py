groups_count = int(input())

musala_percentage = 0
montblanc_percentage = 0
kilimanjaro_percentage = 0
k2_percentage = 0
everest_percentage = 0
total_people = 0

for _ in range(groups_count):
    group_size = int(input())
    total_people += group_size

    if group_size <= 5:
        musala_percentage += group_size
    elif group_size <= 12:
        montblanc_percentage += group_size
    elif group_size <= 25:
        kilimanjaro_percentage += group_size
    elif group_size <= 40:
        k2_percentage += group_size
    elif group_size > 40:
        everest_percentage += group_size

print(f"{(musala_percentage / total_people) * 100:.2f}%")
print(f"{(montblanc_percentage / total_people) * 100:.2f}%")
print(f"{(kilimanjaro_percentage / total_people) * 100:.2f}%")
print(f"{(k2_percentage / total_people) * 100:.2f}%")
print(f"{(everest_percentage / total_people) * 100:.2f}%")

