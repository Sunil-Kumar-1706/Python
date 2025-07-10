#Minimum Rotations to Get the Original String

def min_rotations(s):
    original = s
    n = len(s)
    rotated = s
    for i in range(1, n + 1):
        rotated = rotated[-1] + rotated[:-1]
        if rotated == original:
            return i

s = "abcde"
print(min_rotations(s))
