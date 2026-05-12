username = input()
password = input()

password_chek = input()

while password_chek != password:
    password_chek = input()

print(f"Welcome {username}!")