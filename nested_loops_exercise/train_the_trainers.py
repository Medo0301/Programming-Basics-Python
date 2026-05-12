judges_count = int(input())
presentation_count = 0
total_avg_grade = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    grade_sum = 0
    for _ in range(judges_count):
        grade = float(input())
        grade_sum += grade

    presentation_count += 1
    total_avg_grade += grade_sum / judges_count
    print(f"{presentation_name} - {grade_sum / judges_count:.2f}.")

print(f"Student's final assessment is {total_avg_grade / presentation_count:.2f}.")