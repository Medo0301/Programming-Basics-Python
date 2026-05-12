count_numbers = int(input())

last_pair_sum = 0
max_diff = 0
pair_sum = 0

for idx in range(count_numbers):
    first_num = int(input())
    second_num = int(input())

    if idx == 0:
        last_pair_sum = first_num + second_num
    else:
        pair_sum = first_num + second_num
        if max_diff < abs(last_pair_sum - pair_sum):
            max_diff = abs(last_pair_sum - pair_sum)
        last_pair_sum = pair_sum


if max_diff == 0:
    print(f"Yes, value={last_pair_sum}")
else:
    print(f"No, maxdiff={max_diff}")


# last_pair_sum = 0
# max_diff = 0
# pair_sum = 0
#
# for idx in range(count_numbers * 2):
#     number = int(input())
#     pair_sum += number
#     if idx % 2 != 0:
#         if idx == 1:
#             last_pair_sum = pair_sum
#         else:
#             current_diff = abs(pair_sum - last_pair_sum)
#             if current_diff > max_diff:
#                 max_diff = current_diff
#         last_pair_sum = pair_sum
#         pair_sum = 0
#
# if max_value == min_value:
#     print(f"Yes, value={max_value}")
# else:
#     print(f"No, maxdiff={max_value - min_value}")