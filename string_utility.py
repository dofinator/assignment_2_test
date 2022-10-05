import copy


def upper_letters(s):
    s = list(s)
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for index, letter in enumerate(s):
        if letter in lowercase:
            position = lowercase.find(letter)
            upper = uppercase[position]
            s[index] = upper
    return "".join(s)


def lower_letters(s):
    s = list(s)
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for index, letter in enumerate(s):
        if letter in uppercase:
            position = uppercase.find(letter)
            lower = lowercase[position]
            s[index] = lower
    return "".join(s)

def reverse_string(s):
    str = ""
    for i in s:
        str = i + str
        print(str)
    return str
   