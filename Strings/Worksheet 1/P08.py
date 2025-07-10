'''Find the Maximum Frequency Character
Explanation: Determine which character appears most frequently in the string.
Input: "banana"
Expected Output: Maximum frequency character: 'a' '''

from collections import Counter

def maximum_freq(s):
    counts = Counter(s)
    return max(counts,key=counts.get)
   
s=input("Enter the string: ")
print(f"The character having maximum frequency {maximum_freq(s)}")