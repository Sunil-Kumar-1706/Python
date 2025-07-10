# Write a Python function to find the k-th smallest element in a list.

def small(l,k):
    l.sort()
    return l[k-1]
    
l=[7, 10, 4, 3, 20, 15]
k=int(input("Enter the k value: "))
print(small(l,k))