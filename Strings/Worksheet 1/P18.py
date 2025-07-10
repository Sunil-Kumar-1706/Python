#Print the Middle Character of a String

def mid(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]

i = input("Enter the string: ")
print(mid(i))