#Rotate a String by k Positions

def rotate(s,k):
    k=k%len(s)
    return s[-k:]+s[:-k]

s=input("Enter the string: ")
k=int(input("Enter the k value: "))
res = rotate(s,k)
print(res)