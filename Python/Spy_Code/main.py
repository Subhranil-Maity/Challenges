n = input()[::-1]
b = ""
for c in n:
    if c == " " or c.isalpha():
        b += c
print(b)
