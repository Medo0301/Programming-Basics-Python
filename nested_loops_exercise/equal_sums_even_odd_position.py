first_number = int(input())
second_number = int(input())

for num in range(first_number, second_number + 1):
    temp_num = num
    sum_odd = 0
    sum_even = 0

    for _ in range(3):
        sum_even += temp_num % 10
        temp_num //= 10
        sum_odd += temp_num % 10
        temp_num //= 10

    if sum_even == sum_odd:
        print(num, end=" ")
