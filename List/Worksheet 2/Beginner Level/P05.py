'''
Write a Python program to count the number of strings where the string length is 2 or more 
and the first and last character are the same from a given list of strings.
'''
l=['xyz','aba','abc','121']
c=0
for i in l:
    if len(i)>=2 and i[0]==i[len(i)-1]:
        c+=1
print(c)

