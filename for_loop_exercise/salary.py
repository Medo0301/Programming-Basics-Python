FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

open_tabs_count = int(input())
salary = int(input())

for tab in range(open_tabs_count):
    website_name = input()
    if website_name == "Facebook":
        salary -= FACEBOOK_FINE
    elif website_name == "Instagram":
        salary -= INSTAGRAM_FINE
    elif website_name == "Reddit":
        salary -= REDDIT_FINE

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)