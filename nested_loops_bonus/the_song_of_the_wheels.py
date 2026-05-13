control_value = int(input())
count = 0
password = ''

for digit_a in range(1, 10):
    for digit_b in range(1, 10):
        if digit_a >= digit_b:
            continue
        for digit_c in range(1, 10):
            for digit_d in range(1, 10):
                if digit_c <= digit_d:
                    continue

                if digit_a * digit_b + digit_c * digit_d == control_value:
                    print(f"{digit_a}{digit_b}{digit_c}{digit_d}", end=" ")
                    count += 1
                    if count == 4:
                        password = f"{digit_a}{digit_b}{digit_c}{digit_d}"

print()

if count >= 4:
    print(f"Password: {password}")
else:
    print("No!")