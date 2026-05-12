from sys import maxsize

inpt = input()
max_num = -maxsize

while inpt != "Stop":
    number = int(inpt)
    if max_num < number:
        max_num = number

    inpt = input()

print(max_num)