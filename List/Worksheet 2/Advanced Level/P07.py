# Write a Python function to remove duplicates from a list while preserving the original order of the remaining elements

def rem(l):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s

l=[1,2,2,3,4,3,4,5,6,5]
print(rem(l))