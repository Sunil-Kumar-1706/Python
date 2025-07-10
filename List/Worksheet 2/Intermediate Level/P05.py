# Write a Python program to remove all occurrences of a specific element from a list.

l=[1,2,3,2,4,2,5]
e=2
for i in l:
    if i==e:
        l.remove(i)
print(l)