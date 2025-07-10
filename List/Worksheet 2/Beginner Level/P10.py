# Write a Python program to find the list of words that are longer than n from a given list of words.

l=['hello', 'world', 'python', 'is', 'great']
n=4
m=[i for i in l if len(i)>n]
print(m)