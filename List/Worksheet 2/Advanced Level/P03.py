# Write a Python function that generates all the permutations of the elements in a given list

import itertools

def permut(l):
    return list(itertools.permutations(l))

i=[1,2,3]
l=permut(i)
print(l)