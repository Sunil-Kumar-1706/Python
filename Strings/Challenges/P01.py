'''
Count Number of Kernel Panics and Oops
Description: Given a string containing kernel logs, count how many times "kernel panic" and "Oops" appear (case-insensitive)'''

def count_kernel_issues(log):
    log_lower = log.lower()
    panic_count = log_lower.count("kernel panic")
    oops_count = log_lower.count("oops")
    return panic_count, oops_count

log = """
[12345.67] kernel panic - not syncing: Fatal exception
[12345.89] Oops: 0002 [#1] SMP
[12346.00] kernel panic - not syncing: Fatal exception
[12346.13] Oops: 0003 [#2] SMP
"""

panic, oops = count_kernel_issues(log)
print(f"Kernel panics: {panic}")
print(f"Oops events: {oops}")
