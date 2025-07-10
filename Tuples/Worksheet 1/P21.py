#  Sort a list of (name, age) tuples by the second element (age) in ascending order

lst = [("Alice", 25), ("Bob", 20), ("Eve", 22)]
lst = sorted(lst,key = lambda x: x[1])
print(lst)