'''
Top 3 Most Frequent Error Keywords
Description: Given a kernel log string, count the most frequent error keywords: "fail", "error", "timeout", "panic" (case-insensitive). 
Show the top 3 with their counts.'''

from collections import Counter

def top_error_keywords(log):
    keywords = ["fail", "error", "timeout", "panic"]
    log_lower = log.lower()
    
    counts = Counter()
    for keyword in keywords:
        counts[keyword] = log_lower.count(keyword)
    
    return counts.most_common(3)

log = """
[1.11] ERROR: device failed to start
[1.12] ERROR: timeout waiting for response
[1.13] WARNING: low battery
[1.14] PANIC: unrecoverable error
[1.15] device fail detected
[1.16] timeout on bus
"""

top_errors = top_error_keywords(log)
for word, count in top_errors:
    print(f"{word}: {count}")
