'''
Write a Python program to remove duplicates from a list.
'''

l=[1, 2, 3, 2, 4, 3, 5]
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)
    