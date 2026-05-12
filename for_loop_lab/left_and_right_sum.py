n = int(input())

sum_left = 0
sum_right = 0

for idx in range(n * 2):
    number = int(input())
    if idx < n:
        sum_left += number
    else:
        sum_right += number

if sum_right == sum_left:
    print(f"Yes, sum = {sum_right}")
else:
    print(f"No, diff = {abs(sum_right - sum_left)}")