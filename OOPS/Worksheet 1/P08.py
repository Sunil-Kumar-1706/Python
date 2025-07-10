#Check if Bus is a subclass of Vehicle

class vehicle:
    pass
class bus(vehicle):
    pass

print(issubclass(bus,vehicle))