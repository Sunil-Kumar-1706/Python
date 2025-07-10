# Add an item to a tuple by converting it to a list and back to a tuple.
t=(1,2,3)
t=list(t)
t.append(4)
t=tuple(t)
print(t)