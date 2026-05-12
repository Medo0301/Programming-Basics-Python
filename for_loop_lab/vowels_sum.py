A = 1
E = 2
I = 3
O = 4
U = 5

text = input()

sum = 0

for char in text:
    if char == "a":
        sum += A
    elif char == "e":
        sum += E
    elif char == "i":
        sum += I
    elif char == "o":
        sum += O
    elif char == "u":
        sum += U

print(sum)
