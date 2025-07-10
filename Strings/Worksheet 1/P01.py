#Check if a String is a Palindrome or Symmetrical

def is_palindrome(s):
    return s == s[::-1]

def is_symmetrical(s):
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1:]

s = input("Enter a string: ")

if is_palindrome(s):
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")

if is_symmetrical(s):
    print("The string is Symmetrical.")
else:
    print("The string is NOT Symmetrical.")
