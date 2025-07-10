# Write a Python function to reverse a list at a specific location.

def rev(l,p):
    return l[:p]+l[p:][::-1]


l=[1,2,3,4,5,6]
p=int(input("Enter the p value: "))
print(rev(l,p))
