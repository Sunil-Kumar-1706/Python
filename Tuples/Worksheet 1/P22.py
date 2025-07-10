#  Sort a list of tuples by the total number of digits across all elements in each tuple

def fun(t):
    return sum(len(str(x)) for x in t)

t=[(1, 2), (10, 11), (3, 44)]

t=sorted(t,key = fun)
print(t)