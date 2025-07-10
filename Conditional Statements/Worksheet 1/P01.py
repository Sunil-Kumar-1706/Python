#Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
#(Nominal is between 3.0V and 3.3V inclusive.)

x=float(input("Enter the reading: "))
if x>=3.0 and x<=3.3:
    print("Nominal")
elif x>3.3:
    print("Over Voltage")
else:
    print("Under Voltage")