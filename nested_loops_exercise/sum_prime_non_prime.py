prime_nums_sum = 0
non_prime_nums_sum = 0

while True:
    command = input()

    if command == "stop":
        break
    num = int(command)

    if num < 0:
        print("Number is negative.")
        continue

    if (num == 0) or (num == 1):
        non_prime_nums_sum += num
    elif num > 1:
        is_prime = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_nums_sum += num
        else:
            non_prime_nums_sum += num

print(f"Sum of all prime numbers is: {prime_nums_sum}")
print(f"Sum of all non prime numbers is: {non_prime_nums_sum}")