'''
Highlight All Error Lines and Show Context
Description: For each line containing "error" (case-insensitive), 
print that line plus the previous and next line for context
'''

def highlight_error_context(log):
    lines = log.strip().split('\n')
    for i, line in enumerate(lines):
        if "error" in line.lower():
            start = max(i - 1, 0)
            end = min(i + 1, len(lines) - 1)
            
            for j in range(start, end + 1):
                print(lines[j])
            print()  

log = """
[10.00] Starting system
[10.05] Initializing drivers
[10.10] ERROR: Device not found
[10.15] Trying next device
[10.20] ERROR: Timeout waiting for response
[10.25] Reboot recommended
"""

highlight_error_context(log)
