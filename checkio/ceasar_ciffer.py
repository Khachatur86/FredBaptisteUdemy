def caesar(string, step):
    str_lower = "abcdefghijklmnopqrstuvwxyz"
    str_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    res = ""

    for char in string:
        if char.isupper():
            res += str_upper[(str_upper.find(char) + step) % len(str_upper)]
        elif char.islower():
            res += str_lower[(str_lower.find(char) + step) % len(str_lower)]
        else:
            res += char

    return res