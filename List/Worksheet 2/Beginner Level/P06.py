'''
Write a Python program to get a list, 
sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.'''

l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l=sorted(l,key = lambda x: x[-1])
print(l)