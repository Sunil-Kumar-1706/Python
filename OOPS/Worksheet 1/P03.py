#Log Session a Vehicle class and a Bus class that inherits from it. Demonstrate shared behavior.

class vehicle:
    def move(self):
        print("Vehicle is Moving")
    
class bus(vehicle):
    pass


b=bus()
b.move()