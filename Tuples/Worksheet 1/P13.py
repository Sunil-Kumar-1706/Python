#  Remove a specific element from a tuple by converting it to a list and back

t=(1,2,3,4)
t=list(t)
t.remove(2)
t=tuple(t)
print(t)