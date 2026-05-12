start_char = input()
final_char = input()
non_include_char = input()
skip = ord(non_include_char)
count = 0

for char_1 in range(ord(start_char), ord(final_char) + 1):
    if char_1 == skip:
        continue
    for char_2 in range(ord(start_char), ord(final_char) + 1):
        if char_2 == skip:
            continue
        for char_3 in range(ord(start_char), ord(final_char) + 1):
            if char_3 == skip:
                continue
            count += 1
            print(f"{chr(char_1)}{chr(char_2)}{chr(char_3)}", end=" ")

print(count)