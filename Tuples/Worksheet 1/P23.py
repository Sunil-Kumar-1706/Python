# Change the last value in every tuple in a list to a given value.

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100

l = [t[:-1] + (new_value,) for t in l]

print(l)
