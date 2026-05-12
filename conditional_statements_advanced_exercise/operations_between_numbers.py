first_number = int(input())
second_number = int(input())
math_operator = input()

answer = ""

if math_operator == "+":
    answer = (f"{first_number} {math_operator} {second_number} = {first_number + second_number}"
              f"{'- even' if (first_number + second_number) % 2 == 0 else '- odd'}")
elif math_operator == "-":
    answer = (f"{first_number} {math_operator} {second_number} = {first_number - second_number}"
              f"{'- even' if (first_number - second_number) % 2 == 0 else '- odd'}")
elif math_operator == "*":
    answer = (f"{first_number} {math_operator} {second_number} = {first_number * second_number}"
              f"{'- even' if (first_number * second_number) % 2 == 0 else '- odd'}")
elif second_number == 0:
    answer = f"Cannot divide {first_number} by zero"
elif math_operator == "/":
    answer = f"{first_number} {math_operator} {second_number} = {first_number / second_number:.2f}"
elif math_operator == "%":
    answer = f"{first_number} {math_operator} {second_number} = {first_number % second_number}"

print(answer)