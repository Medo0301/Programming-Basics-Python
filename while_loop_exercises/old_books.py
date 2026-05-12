the_book = input()
chek_counter = 0
found = False

next_book = input()

while next_book != "No More Books":
    if next_book == the_book:
        found = True
        break
    chek_counter += 1
    next_book = input()

if found:
    print(f"You checked {chek_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {chek_counter} books.")