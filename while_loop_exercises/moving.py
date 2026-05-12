width = int(input())
length = int(input())
height = int(input())

space = width * length * height
is_done = False

while space > 0:
    boxes = input()
    if boxes == "Done":
        is_done = True
        break

    space -= int(boxes)

if is_done:
    print(f"{space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space)} Cubic meters more.")