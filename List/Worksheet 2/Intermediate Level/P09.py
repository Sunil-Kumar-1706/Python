# Write a Python program to create a list of numbers from 1 to 20, 
# where each number is squared if it is even, and cubed if it is odd.

s=[i**2 if i%2==0 else i**3 for i in range(1,21)]
print(s)