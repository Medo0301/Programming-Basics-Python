bad_grades_limit = int(input())

grade_sum = 0.0
grade_counter = 0
bad_grade = 0
last_problem = ''
failed = False

while True:
    problem_name = input()
    if problem_name == "Enough":
        break
    grade = float(input())

    if grade <= 4:
        bad_grade += 1
        if bad_grade == bad_grades_limit:
            failed = True
            break

    grade_sum += grade
    grade_counter += 1
    last_problem = problem_name

if failed:
    print(f"You need a break, {bad_grade} poor grades.")
else:
    print(f"Average score: {grade_sum / grade_counter:.2f}")
    print(f"Number of problems: {grade_counter}")
    print(f"Last problem: {last_problem}")
