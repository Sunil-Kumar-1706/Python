# Remove all empty tuples from a list of tuples and print the cleaned list.

l=[(), (), ('a', 'b'), ('c',)]
l=[i for i in l if i]
print(l)