barcode_range_start = int(input())
barcode_range_final = int(input())

range_start_to_str = str(barcode_range_start)
range_final_to_str = str(barcode_range_final)

for digit_1 in range(int(range_start_to_str[0]), int(range_final_to_str[0]) + 1):
    if digit_1 % 2 == 0:
        continue
    for digit_2 in range(int(range_start_to_str[1]), int(range_final_to_str[1]) + 1):
        if digit_2 % 2 == 0:
            continue
        for digit_3 in range(int(range_start_to_str[2]), int(range_final_to_str[2]) + 1):
            if digit_3 % 2 == 0:
                continue
            for digit_4 in range(int(range_start_to_str[3]), int(range_final_to_str[3]) + 1):
                if digit_4 % 2 == 0:
                    continue

                print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end=" ")
