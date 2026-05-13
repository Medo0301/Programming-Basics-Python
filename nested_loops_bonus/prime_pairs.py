first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

first_pair_end = first_pair_start + first_pair_diff
second_pair_end = second_pair_start + second_pair_diff

for num in range(first_pair_start, first_pair_end + 1):
    is_first_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_first_prime = False
            break
    if is_first_prime:
        for num_2 in range(second_pair_start, second_pair_end + 1):
            is_second_prime = True
            for i in range(2, int(num_2 ** 0.5) + 1):
                if num_2 % i == 0:
                    is_second_prime = False
                    break

            if is_second_prime:
                print(f"{num}{num_2}")

