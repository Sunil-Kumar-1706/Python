# Write a Python program to flatten a shallow list.

l= [[1, 2], [3, 4], [5, 6]]
s=[j for i in l for j in i]
print(s)