first_num = int(input())
second_num = int(input())

for num_1 in range(1, first_num):
    for num_2 in range(1, first_num):
        for char_1 in range(ord('a'), ord('a') + second_num):
            for char_2 in range(ord('a'), ord('a') + second_num):
                for num_3 in range(1, first_num + 1):
                    if num_3 > num_1 and num_3 > num_2:
                        print(f"{num_1}{num_2}{chr(char_1)}{chr(char_2)}{num_3}", end=" ")