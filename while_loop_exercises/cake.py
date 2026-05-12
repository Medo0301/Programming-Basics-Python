width = int(input())
length = int(input())

pieces = width * length
has_pieces = False

while pieces > 0:
    taken_pieces = input()
    if taken_pieces == "STOP":
        has_pieces = True
        break

    pieces -= int(taken_pieces)

if has_pieces:
    print(f"{pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
