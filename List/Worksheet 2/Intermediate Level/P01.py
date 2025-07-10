# Write a Python program to find the common elements between two lists.

l1=[1,2,3,4]
l2=[2,6,3,7]
c=list(set(l1)&set(l2))
print(c)