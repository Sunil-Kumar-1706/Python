# Write a Python program to unzip a list of tuples into individual lists

l=[(1, 'a'), (2, 'b'), (3, 'c')]
l1,l2=zip(*l)
l1=list(l1)
l2=list(l2)
print(l1,l2)