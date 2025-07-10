#Find the Length of a String
def length(s):
    c=0
    for i in s:
        c+=1
    return c

s=input("Enter the string: ")
print(length(s))