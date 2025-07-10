# Convert a tuple of characters to a string and then back to a tuple
t=('s','u','n','i','l')
t=''.join(t)
print(t)
t=tuple(t)
print(t)