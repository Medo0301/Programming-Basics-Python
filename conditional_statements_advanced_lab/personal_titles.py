age = float(input())
gender = input()
titles = ""

if gender == "m":
    if age >= 16:
        titles = "Mr."
    else:
        titles = "Master"
else:
    if age >= 16:
        titles = "Ms."
    else:
        titles = "Miss"

print(titles)