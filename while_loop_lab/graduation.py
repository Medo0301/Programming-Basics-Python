name = input()
count_class = 1
fails_count = 0
grades_sum = 0.0

while count_class <= 12:
    grade = float(input())

    if grade < 4:
        if fails_count >= 1:
            break
        else:
            fails_count += 1
            continue

    grades_sum += grade
    count_class += 1

if count_class <= 12:
    print(f"{name} has been excluded at {count_class} grade")
else:
    print(f"{name} graduated. Average grade: {grades_sum / 12:.2f}")