students_count = int(input())
average_grade = 0
fail_percentage = 0
between_3_and_4_percentage = 0
between_4_and_5_percentage = 0
top_students_percentage = 0

for _ in range(students_count):
    grade = float(input())
    average_grade += grade
    if grade < 3:
        fail_percentage += 1
    elif grade < 4:
        between_3_and_4_percentage += 1
    elif grade < 5:
        between_4_and_5_percentage += 1
    else:
        top_students_percentage += 1

print(f"Top students: {(top_students_percentage / students_count) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(between_4_and_5_percentage / students_count) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(between_3_and_4_percentage / students_count) * 100:.2f}%")
print(f"Fail: {(fail_percentage / students_count) * 100:.2f}%")
print(f"Average: {average_grade / students_count:.2f}")
