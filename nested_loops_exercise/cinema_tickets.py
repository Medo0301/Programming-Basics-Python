total_tickets = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0

while True:
    film_name = input()
    if film_name == "Finish":
        break

    free_seats = int(input())
    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0
    for _ in range(free_seats):
        type_tickets = input()
        if type_tickets == "End":
            break
        elif type_tickets == "student":
            student_tickets += 1
        elif type_tickets == "standard":
            standard_tickets += 1
        elif type_tickets == "kid":
            kid_tickets += 1

    total_sell_tickets_for_movie = student_tickets + standard_tickets + kid_tickets
    print(f"{film_name} - {(total_sell_tickets_for_movie / free_seats) * 100:.2f}% full.")
    total_tickets += total_sell_tickets_for_movie
    total_student_tickets += student_tickets
    total_standard_tickets += standard_tickets
    total_kid_tickets += kid_tickets

print(f"Total tickets: {total_tickets}")
print(f"{(total_student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(total_standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(total_kid_tickets / total_tickets) * 100:.2f}% kids tickets.")
