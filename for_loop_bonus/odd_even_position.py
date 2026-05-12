import sys

numbers = int(input())
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_min = sys.maxsize
even_max = -sys.maxsize
odd_sum = 0
even_sum = 0

for idx in range(1, numbers + 1):
    num = float(input())
    if idx % 2 != 0:
        odd_sum += num
        if odd_min > num:
            odd_min = num
        if odd_max < num:
            odd_max = num

    else:
        even_sum += num
        if even_min > num:
            even_min = num
        if even_max < num:
            even_max = num

print(f"OddSum={odd_sum:.2f},")

if odd_min == sys.maxsize:
    print("OddMin=No,")
    print("OddMax=No,")
else:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")

if even_min == sys.maxsize:
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")