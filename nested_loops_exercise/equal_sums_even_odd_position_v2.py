start = int(input())
end = int(input())

for num in range(start, end + 1):
    num_to_str = str(num)
    even_sum = 0
    odd_sum = 0

    for idx, digit in enumerate(num_to_str):
        if idx % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if odd_sum == even_sum:
        print(num, end=" ")