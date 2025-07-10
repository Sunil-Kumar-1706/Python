#Count Frequency of Words in String (Short Form)

from collections import Counter

text = "apple apple orange"
freq = Counter(text.split())
print(dict(freq))
