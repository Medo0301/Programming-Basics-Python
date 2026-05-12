exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_minutes = (exam_hour * 60) + exam_minutes
arrival_minutes = (arrival_hour * 60) + arrival_minutes

arrival = ""
answer = ""

if exam_minutes < arrival_minutes:
    arrival = "Late"

    if arrival_minutes - exam_minutes < 60:
        answer = f"{arrival_minutes - exam_minutes} minutes after the start"
    else:
        late_by = arrival_minutes - exam_minutes
        answer = f"{late_by // 60}:{late_by % 60:02d} hours after the start"

elif exam_minutes == arrival_minutes:
    arrival = "On time"

elif exam_minutes - arrival_minutes <= 30:
    arrival = "On time"
    answer = f"{exam_minutes - arrival_minutes} minutes before the start"

elif exam_minutes - arrival_minutes > 30:
    arrival = "Early"

    if exam_minutes - arrival_minutes < 60:
        answer = f"{exam_minutes - arrival_minutes} minutes before the start"
    else:
        time_diff = exam_minutes - arrival_minutes
        answer = f"{time_diff // 60}:{time_diff % 60:02d} hours before the start"

print(arrival)
print(answer)
# if exam_hour == arrival_hour:
#     if exam_minutes == arrival_minutes:
#         arrival = "On time"
#     elif exam_minutes > arrival_minutes and exam_minutes - arrival_minutes <= 30:
#         arrival = "On time"
#         answer = f"{exam_minutes - arrival_minutes} minutes before the start"
#     elif exam_minutes < arrival_minutes:
#         arrival = "Late"
#         answer = f"{arrival_minutes - exam_minutes} minutes after the start"
#     elif exam_minutes > arrival_minutes and exam_minutes - arrival_minutes > 30:
#         arrival = "Early"
#         answer = f"{exam_minutes - arrival_minutes} minutes before the start"
# elif exam_hour > arrival_hour:
#     if (exam_hour - arrival_hour == 1
#             and exam_minutes < arrival_minutes
#             and (exam_minutes - arrival_minutes + 60 <= 30)):
#         arrival = "On time"
#         answer = f"{exam_minutes - arrival_minutes + 60} minutes before the start"
#     elif (exam_hour - arrival_hour == 1
#           and exam_minutes < arrival_minutes
#           and (exam_minutes - arrival_minutes + 60 > 30)):
#         arrival = "Early"
#         answer = f"{exam_minutes - arrival_minutes + 60} minutes before the start"
#     elif exam_minutes >= arrival_minutes:
#         arrival = "Early"
#         answer = f"{exam_hour - arrival_hour}:{exam_minutes - arrival_minutes:02d} hours before the start"
#     elif exam_minutes < arrival_minutes:
#         arrival = "Early"
#         answer = f"{exam_hour - arrival_hour - 1}:{exam_minutes - arrival_minutes + 60:02d} hours before the start"
# elif exam_hour < arrival_hour:
#     arrival = "Late"
#     if arrival_hour - exam_hour == 1 and exam_minutes > arrival_minutes:
#         answer = f"{arrival_minutes - exam_minutes + 60} minutes after the start"
#     elif exam_minutes > arrival_minutes:
#         answer = f"{arrival_hour - exam_hour}:{arrival_minutes - exam_minutes + 60} hours after the start"
#     else:
#         answer = f"{arrival_hour - exam_hour}:{arrival_minutes - exam_minutes} hours after the start"

