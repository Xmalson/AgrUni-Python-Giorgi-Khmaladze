row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"

action = input("Enter action (e/d): ").strip().lower()



if action not in ("e", "d"):
    print("Invalid action!")
else:
    text = input("Enter text: ")
    result = ""
    for ch in text:
        if ch.islower():
            if ch in row1:
                row = row1
            elif ch in row2:
                row = row2
            elif ch in row3:
                row = row3
            else:
                result += ch
                continue

            idx = row.index(ch)
            if action == "e":
                new_char = row[(idx + 1) % len(row)]
            else:
                new_char = row[(idx - 1) % len(row)]
            result += new_char
        else:
            result += ch
    print(result)
