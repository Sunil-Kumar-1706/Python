'''Description: Given a list of pairs (tuples), separate each position into its own list (unzipping).
Unzipping is key for parallel data processing and converting between row-wise and column-wise formats.
Input: lst = [(1, 'a'), (2, 'b'), (3, 'c')]
Output: [1, 2, 3]
['a', 'b', 'c']'''
import ast
t=input("Enter the list of tuple:")
t=ast.literal_eval(t)

a,b=zip(*t)
a=list(a)
b=list(b)
print(a,' ',b)