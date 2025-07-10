#Check if a Bus object is an instance of Vehicle

class vehicle:
    pass
class bus(vehicle):
    pass

b=bus()
print(isinstance(b,vehicle))