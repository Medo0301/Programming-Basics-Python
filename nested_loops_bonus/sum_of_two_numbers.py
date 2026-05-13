start_interval = int(input())
end_interval = int(input())
magic_num = int(input())

isFound = False
count = 0

for num_1 in range(start_interval, end_interval + 1):
    for num_2 in range(start_interval, end_interval + 1):
        count += 1
        if num_1 + num_2 == magic_num:
            print(f"Combination N:{count} ({num_1} + {num_2} = {magic_num})")
            isFound = True
            break

    if isFound:
        break

if not isFound:
    print(f"{count} combinations - neither equals {magic_num}")

