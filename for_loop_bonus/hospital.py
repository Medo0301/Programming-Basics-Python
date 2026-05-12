doctors_count = 7
period = int(input())
treated_patients = 0
untreated_patients = 0

for day in range(1, period + 1):
    patients_for_the_day = int(input())
    if day % 3 == 0 and treated_patients < untreated_patients:
        doctors_count += 1
    if patients_for_the_day <= doctors_count:
        treated_patients += patients_for_the_day
    else:
        treated_patients += doctors_count
        untreated_patients += patients_for_the_day - doctors_count

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
