'''
Extract All Lines Containing WARNING With Timestamps
Description: From a multiline log string, print all lines that include the word "WARNING" (case-insensitive), including their timestamps.'''

def extract_warning_lines(log):
    lines = log.strip().split('\n')
    warning_lines = [line for line in lines if "warning" in line.lower()]
    return warning_lines

log = """
[100.123] INFO: Booting Linux
[100.456] WARNING: Low memory detected
[101.000] WARNING: CPU load high
[101.555] INFO: Boot complete
"""

warnings = extract_warning_lines(log)
for line in warnings:
    print(line)
