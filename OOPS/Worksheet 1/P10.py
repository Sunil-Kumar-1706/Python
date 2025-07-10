#Build a Circle class with area() and perimeter() methods.

import math
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def perimeter(self):
        return 2*math.pi*self.r

x=circle(2)
print(x.area(),x.perimeter())