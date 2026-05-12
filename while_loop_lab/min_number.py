from sys import maxsize

inpt = input()
min_num = maxsize

while inpt != "Stop":
    number = int(inpt)
    if min_num > number:
        min_num = number

    inpt = input()

print(min_num)