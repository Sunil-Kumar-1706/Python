# Write a Python function to find the union and intersection of two lists.

def union_inter(a,b):
    a=set(a)
    b=set(b)
    union=list(a|b)
    inter=list(a&b)
    return union,inter


a=[1,2,3,4]
b=[3,4,5,6]
union,inter=union_inter(a,b)
print("Union :",union)
print("intersection :",inter)