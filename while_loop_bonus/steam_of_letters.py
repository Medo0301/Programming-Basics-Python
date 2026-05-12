c_found = False
o_found = False
n_found = False

word = ""

while True:
    char = input()

    if char == "End":
        break

    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        if char == 'c' and not c_found:
            c_found = True
        elif char == 'o' and not o_found:
            o_found = True
        elif char == 'n' and not n_found:
            n_found = True
        else:
            word += char

        if c_found and o_found and n_found:
            print(word, end=" ")
            word = ""
            c_found = False
            o_found = False
            n_found = False
