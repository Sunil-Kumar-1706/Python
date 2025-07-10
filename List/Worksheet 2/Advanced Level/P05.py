# Write a Python function to check if a given list is a palindrome (reads the same forwards and backwards).

def pal(l):
    return l==l[::-1]

l=[1,2,3,2,1]
print(pal(l))