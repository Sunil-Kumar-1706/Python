'''
Print All Plug/Unplug USB Events
Description: Print all lines that indicate a USB device was plugged in or unplugged 
(look for "USB disconnect" or "new full-speed USB device" in the log lines)
'''

def extract_usb_events(log):
    lines = log.strip().split('\n')
    usb_events = [line for line in lines if 
                  "usb disconnect" in line.lower() or 
                  "new full-speed usb device" in line.lower()]
    return usb_events

log = """
[22.1] usb 1-1: USB disconnect, device number 2
[22.3] usb 1-1: new full-speed USB device number 3 using xhci_hcd
[22.5] usb 2-1: reset high-speed USB device number 4 using ehci-pci
"""

events = extract_usb_events(log)
for event in events:
    print(event)
