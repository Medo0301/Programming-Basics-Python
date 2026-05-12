inpt = input()
total_sum = 0.0

while inpt != "NoMoreMoney":
    sum = float(inpt)
    if sum < 0:
        print("Invalid operation!")
        break
    total_sum += sum
    print(f"Increase: {sum:.2f}")

    inpt = input()

print(f"Total: {total_sum:.2f}")