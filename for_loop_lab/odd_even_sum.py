n = int(input())

sum_odd = 0
sum_even = 0

for idx in range(n):
    number = int(input())
    if idx % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

if sum_odd == sum_even:
    print(f"Yes\nSum = {sum_odd}")
else:
    print(f"No\nDiff = {abs(sum_odd - sum_even)}")