num_x = int(input())
num_y = int(input())
max_passwords = int(input())

char_a = 35
char_b = 64
counter = 0

has_reached_limit = False

for idx1 in range(1, num_x + 1):
    for idx2 in range(1, num_y + 1):
        print(f"{chr(char_a)}{chr(char_b)}{idx1}{idx2}{chr(char_b)}{chr(char_a)}", end="|")
        counter += 1
        char_a += 1
        char_b += 1

        if counter == max_passwords:
            has_reached_limit = True
            break

        if char_a > 55:
            char_a = 35

        if char_b > 96:
            char_b = 64

    if has_reached_limit:
        break
