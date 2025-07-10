# Identify and print elements that occur more than once in a tuple

from collections import Counter

t=(1,2,3,4,2,3)
c=Counter(t)
t=tuple(i for i,j in c.items() if j>1)
print(t)
